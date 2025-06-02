# Justype's Personal Website

It is actually inspired by those websites emulates old PC systems and with the help of GitHub Copilot.

## How to use

Just clone this repository and change the files in the `content` directory. You can also change the `index.html` file to customize the website.

My `.github/scripts/gen_content_hierarchy.py` will generate a `content-hierarchy.json` file that is used by the File Explorer in `index.html`.

## One thing you need to do

The `index.html` requires `content-hierarchy.json` to be present in the same directory. You can generate it by running the following command:

```bash
# In the root directory of the repository
python .github/scripts/gen_content_hierarchy.py
```

If you are using GitHub Actions, this will be done automatically when you push to the repository. By default it runs perfectly fine, but you may need to set the `GITHUB_TOKEN` secret in your repository settings or change the permissions to allow the action to run.

## LICENSE CC-BY-NC

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. You can view the license [here](https://creativecommons.org/licenses/by-nc/4.0/).

Feel free to use this repository as a template for your own personal website, but please do not use it for commercial purposes.
