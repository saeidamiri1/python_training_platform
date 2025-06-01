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
VS Code is a free, modern, and powerful integrated development environment (IDE) developed by Microsoft. It is available for Windows, Linux, macOS, and even web browsers. VS Code is widely used for coding, debugging, and managing projects in various programming languages, including Python, Bash, and more.

After spending a significant amount of time coding and editing with VS Code, I would like to share my setup and recommendations. Once you install it, follow these steps to optimize your experience:

* Connect VSCode to GitHub for seamless version control.
* Choose the right theme to enhance readability and comfort.
* Install essential Python extensions, including: Python, Python Debugger, Python Indent
* Install Python Snippets to speed up coding.
* Install the Jupyter extension for interactive coding with Jupyter notebooks.

By following these steps, you can make the most out of VS Code for your development needs!




