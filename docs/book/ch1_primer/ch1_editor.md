---
title: Editor
---

# Editor
We often use the command line, but users can utilize an interactive Python command line called IPython, which offers more functionality. IPython is a module that can be installed via `pip install ipython`. For instance, by using `!`, system shell commands can be passed directly to Python. Additionally, you can measure the running time of a function using the `%timeit` magic command.

```
(venv) samamiri@Sams-MacBook-Pro ~ % ipython
Python 3.11.10 (main, Sep  7 2024, 01:03:31) [Clang 15.0.0 (clang-1500.3.9.4)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: var=!ls

In [2]: print(var)
['Applications', 'Desktop', 'Documents', 'Downloads', 'Google Drive', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'aa.htlm', 'bin', 'quiztudy.com', 'temp', 'venv']

In [3]: %timeit 2+2
4.82 ns ± 0.00562 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)

```

More details can be found in [ipython documetation. ](https://ipython.readthedocs.io/)


Instead of using the command line, you can choose from several useful editors for Python, such as [VS Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), [IPython](https://ipython.org/), [Jupyter](https://jupyter.org/), [Spyder](https://www.spyder-ide.org/)


## Jupyter
The Jupyter Notebook is a web-based interactive computational environment for programming, used to create and share documents containing live code, equations, visualizations, and narrative text. JupyterLab, the next-generation interface for Project Jupyter, offers a more flexible and powerful user experience. Jupyter saves files with the `.ipynb` extension, which stores the notebook's content. Some editors, such as VS Code (described below), support `.ipynb` files.

## VS Code
VS Code editor is a free and modern  integrated development environment (IDE) developed by the Microsoft and   for Windows, Linux, macOS and web browsers which is used as an editor for coding, debugging, and managing projects in different programming languages, including Python. 

In the following Video, I present how I use vscode to do programming. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/3xHFCpglNxA?si=2S6G0IptvNDfYBzj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>