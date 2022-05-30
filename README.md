# Install and configure Python formating - autopep8

# Install Python dependencies

## 1. Create a requirements.txt file and add the dependencies
```
autopep8
```

## 2. Run pip
```
pip3 install -r requirements.txt
```

## 3. Edit indent size from autopep8
```
code /usr/local/lib/python3.8/dist-packages/code autopep8.py

Search for "DEFAULT_INDENT_SIZE" and change it to 2
```

## New info