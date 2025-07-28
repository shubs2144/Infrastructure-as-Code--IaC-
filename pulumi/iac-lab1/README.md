### setup steps

follow this youtube video to set up the project: https://www.youtube.com/watch?v=EtEb40LE5zQ


### 🔄 **Overview: What this code does**

This script:

1. Creates an AWS S3 bucket configured to serve a **static website**.
2. Uploads all files from a specified local folder (like `public/` or `build/`) into that bucket.
3. Sets appropriate **MIME types** (so the browser knows how to interpret each file).
4. Exports the bucket name and its website endpoint URL.

---

### 🔍 Code Breakdown (Line-by-Line)

#### 1. **Imports**

```python
import pulumi
import pulumi_aws as aws
import os
import mimetypes
```

* `pulumi`: Core Pulumi SDK. Used to define and manage infrastructure resources.
* `pulumi_aws`: Pulumi package to create AWS resources.
* `os`: Python built-in module to interact with the file system.
* `mimetypes`: Helps guess file types (like `text/html` or `image/png`) based on file extensions.

---

#### 2. **Config and Directory Path**

```python
config = pulumi.Config()
site_dir = config.require("siteDir")
```

* `pulumi.Config()` fetches values from Pulumi configuration (`Pulumi.dev.yaml`, etc.).
* `config.require("siteDir")` fetches the `siteDir` key (like `./public`) and throws an error if not found.

  * ✅ Used to define the local folder where website files live.

---

#### 3. **S3 Bucket Creation**

```python
bucket = aws.s3.Bucket("my-bucket",
   website={
       "index_document": "index.html"
})
```

* `aws.s3.Bucket`: Creates a new S3 bucket named `"my-bucket"` in AWS.
* `website={...}`: Enables **static website hosting** on this bucket.

  * `"index_document": "index.html"`: Tells S3 to serve `index.html` when someone visits the root URL.

---

#### 4. **Loop Through Local Files and Upload to S3**

```python
for file in os.listdir(site_dir):
    filepath = os.path.join(site_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
```

* `os.listdir(site_dir)`: Lists all files inside your local static site folder.
* `os.path.join(...)`: Joins directory and filename safely.
* `mimetypes.guess_type(...)`: Returns the MIME type of the file (e.g., `text/html`, `image/png`).

  * ❗ Important so browsers know how to handle files.

---

#### 5. **Create BucketObject for Each File**

```python
    obj = aws.s3.BucketObject(file,
          bucket=bucket.bucket,
          source=pulumi.FileAsset(filepath),
          acl="public-read",
          content_type=mime_type
    )
```

* `aws.s3.BucketObject`: Uploads a file to the S3 bucket.
* `file`: Object key (i.e., the name in S3).
* `bucket=bucket.bucket`: Refers to the bucket we just created.
* `source=pulumi.FileAsset(filepath)`: Uploads a local file to the cloud.
* `acl="public-read"`: Makes the object publicly accessible (⚠️ this may fail if ACLs are disabled — see earlier message).
* `content_type=mime_type`: Tells S3 the file type (so browsers show it correctly).

---

#### 6. **Export Outputs**

```python
pulumi.export('bucket_name', bucket.bucket)
pulumi.export('bucket_endpoint', pulumi.Output.concat("http://", bucket.website_endpoint))
```

* `pulumi.export(...)`: Prints info at the end of deployment.

  * `'bucket_name'`: Name of the S3 bucket.
  * `'bucket_endpoint'`: Full website URL (like `http://my-bucket.s3-website-us-east-1.amazonaws.com`).

---

### 🎯 Purpose

This code:

* Helps you **automate deployment of a static site** (HTML/CSS/JS) to S3.
* No manual file uploads needed.
* Automatically makes the site available publicly via an S3 website endpoint.

---

### ✅ Example Workflow

1. You have a folder like `public/` with `index.html`, `style.css`, etc.
2. Set the config:

   ```bash
   pulumi config set siteDir ./public
   ```
3. Run:

   ```bash
   pulumi up
   ```
4. Your files are uploaded and accessible via an HTTP link!

---

### 💡 Suggested Fix (if ACL error occurs)

Since newer buckets block `acl="public-read"`, remove or ignore that line:

```python
obj = aws.s3.BucketObject(
    file,
    bucket=bucket.bucket,
    source=pulumi.FileAsset(filepath),
    content_type=mime_type,
    opts=pulumi.ResourceOptions(ignore_changes=["acl"])
)
```

Then use **bucket policy** to allow public access if needed.

