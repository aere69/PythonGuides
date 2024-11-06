# Add tcl/tk to virtual environment

To add Tcl to a Python virtual environment (venv), you can follow these steps:

1. Create a Virtual Environment:

    ```py
    python -m venv myenv
    ```

    Replace myenv with your desired environment name.

2. Activate the Virtual Environment:
    + On Windows:

        ```sh
        myenv\Scripts\activate
        ```

    + On macOS/Linux:

        ```sh
        source myenv/bin/activate
        ```

3. Install Tcl/Tk: Tcl/Tk is usually included with Python installations, but you might need to ensure it’s available in your virtual environment. You can copy the Tcl/Tk libraries from your system Python installation to your virtual environment:

    + Locate the Tcl/Tk libraries in your system Python installation. They are typically found in directories like `C:\PythonXX\tcl` on Windows or `/usr/local/lib/tcl8.6` on macOS/Linux.

    + Copy these directories to your virtual environment:

        ```sh
        cp -r /path/to/system/python/tcl myenv/
        ```

4. Set Environment Variables: Ensure your virtual environment can locate the Tcl/Tk libraries by setting the `TCL_LIBRARY` and `TK_LIBRARY` environment variables:

    + On Windows:

        ```sh
        set TCL_LIBRARY=myenv\tcl\tcl8.6
        set TK_LIBRARY=myenv\tcl\tk8.6
        ```

    + On macOS/Linux:

        ```sh
        export TCL_LIBRARY=myenv/tcl/tcl8.6
        export TK_LIBRARY=myenv/tcl/tk8.6
        ```
