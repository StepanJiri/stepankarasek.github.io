# Setup

1. Create a new repository on GitHub, upload all these files.
2. In the repo settings, go to Pages, and set the source to the main branch.
3. Once you own your domain (e.g. sjk.eu), add it under Pages > Custom domain,
   and add a CNAME/ALIAS record at your registrar pointing to
   `yourusername.github.io`.
4. Edit `_layouts/default.html` to fill in your real Mastodon username.
5. To write a new blog post: copy `_posts/2026-08-17-example-post.md`,
   rename it `YYYY-MM-DD-your-title.md`, change the title/image, write
   your article body in markdown below the `---` front matter.
6. Drop images/gifs into `assets/images/` and reference them as
   `/assets/images/filename.gif`.
