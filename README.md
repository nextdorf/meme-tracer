# meme-tracer

The tool identifies which template was used in a meme. It can find in subreddits every post which used a particular template. These findings can then be used to analyze when a meme was first seen, when it was popular, and when it spread to other subreddits. 

## Milestones

<!-- Use "[done]", "[planned]" and "[in progress]" -->
* Compare an image to a template and calculate a likelihood for equality [in progress]
* Connect to a reddit bot [in progress]
* Visualize found reddit posts in a graph/timeline [planned]
* python GUI (with tkinter) [planned]

## Build and install

Build from source with
```
python -m build
```

## Developement

If the package can't figure out the version or complains because `/src/_version.py` doesn't exist, run `python -m setuptools_scm` in the root directory of this package. Also check `git log --tags`.

# See also

[Reddit API Terms and Services](https://docs.google.com/a/reddit.com/forms/d/1ao_gme8e_xfZ41q4QymFqg5HD29HggOD8I9-MFTG7So/viewform)
