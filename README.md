# Justype's Personal Website

It is actually inspired by those websites emulates old PC systems and with the help of GitHub Copilot.

## One thing you need to do

The `index.html` requires `content-hierarchy.json` to be present in the same directory. You can generate it by running the following command:

```bash
# In the root directory of the repository
python .github/scripts/gen_content_hierarchy.py
```

If you are using GitHub Actions, this will be done automatically when you push to the repository. You may need to set the `GITHUB_TOKEN` secret in your repository settings or change the permissions to allow the action to run.
