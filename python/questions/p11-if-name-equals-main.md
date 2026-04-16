Q. What's `if __name__ == "__main__"` for ?

`__name__` is a variable managed by Python. When it runs a file directly, it sets this variable to `"__main__"` whereas when the same file is imported by another module, it sets this variable to the module's name.

Thanks to this, we can know if the curent script was directly executed or is merely imported. 

This is important because we don't want an imported module to execute code right away, we want it to merely expose methods that our code will then execute.