# Shell Command Assignment - Solutions

> **NOTE** In *Windows Command Prompt*, change all `/` symbols to `\` symbols. *Windows Powershell* can be configured so that either `/` or `\` is fine.

Suppose your directory looks like this:

```
.
└── topfolder
    ├── file_one
    ├── file_two
    └── midfolder
        ├── deepfolder
        │   └── deep_file
        ├── file_one
        └── file_two
```

1.
    **In one command**, create a file called `hello.py` in the directory `midfolder` so that your directory looks like this:
    ```
    .
    └── topfolder
        ├── file_one
        ├── file_two
        └── midfolder
            ├── deepfolder
            │   └── deep_file
            ├── file_one
            ├── file_two
            └── hello.py
    ```
    <ul>
        <li>
            **SOLUTION**: The command `touch topfolder/midfolder/hello.py` will create a file called `hello.py` in `topfolder/midfolder`.
        </li>
        <li>
            **BONUS SOLUTION**: The command `rm topfolder/midfolder/hello.py` will remove that file.
        </li>
    </ul>

2.
    **In one command**, create a directory called `sup` in `midfolder` so that your directory looks like this:
    ```
    .
    └── topfolder
        ├── file_one
        ├── file_two
        └── midfolder
            ├── deepfolder
            │   └── deep_file
            ├── file_one
            ├── file_two
            └── sup
    ```
    <ul>
        <li>
            **SOLUTION**: The command `mkdir topfolder/midfolder/sup` will create a folder called `sup` in `topfolder/midfolder`
        </li>
        <li>
            **BONUS SOLUTION**: The command `rm -rf topfolder/midfolder/sup` will remove that folder.
        </li>
    </ul>

3.
    **In two commands**, make your directory look like this:
    ```
    .
    └── topfolder
        ├── file_one
        ├── file_two
        └── midfolder
            ├── another_file
            ├── file_one
            └── file_two
    ```
    <ul>
        <li>
            **SOLUTION**: The command `rm -rf topfolder/midfolder/deepfolder` will remove the directory `topfolder/midfolder/deepfolder`, along with its contents `deep_file`. The command `touch topfolder/midfolder/another_file` will then create `another_file` in `topfolder/midfolder`.
        </li>
        <li>
            **BONUS SOLUTION**: The commands `mkdir topfolder/midfolder/deepfolder` and `touch topfolder/midfolder/deepfolder/deep_file` will re-create `deepfolder` and its contents.
        </li>
    </ul>



