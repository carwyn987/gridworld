# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

Upload to PiPy:

```
python3 -m pip install --upgrade build
python3 -m build # where pyproject.toml is
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/* # username __token__, requires your token including the pypi- prefix.
```

Then you can install with 
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
```
aka
```
pip install -i https://test.pypi.org/simple/ gridworld-carwyn987==0.0.1
```

This will make the files in src accessible by import
```
import example
example.add_one(3)
```