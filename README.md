# Python-GoTo

A PyPi module allowing the users' code to navigate to aliased line number within the Python interpreter

![Generic badge](https://img.shields.io/badge/version-0.0.1-green.svg)

## How does it work?

User import goto to their project:
```python
from goto_plus import *
```
and then complete configuration:
```python
gotoconfig(__file__)
```

## Why goto_plus 

`goto` from goto_plus works with line numbers (labels coming very soon) to allows the user dynamic control over the flow of their python code.

###Example
```python
j = 0
j += 1
print(j)
if j < 10: goto(2)

```

## Installation

On bash:
```bash
$ pip install goto-plus
```

On windows:
```
py -m pip install goto-plus
```

### Manually (NOT RECOMMENDED)
Copy the contents of the file `goto.py` into you project and proceed accordingly

This file can be found here [goto_plus\goto.py](https://github.com/abhinav-gg/goto-plusthon/blob/main/goto_plus/goto.py)

## Usage

* [goto calendar example](#goto-calendar-example)
* [Contributing](#Contributing)


### goto calendar example
To goto calendar example, type:
```bash
goto(line)
```

#### Example:
__IN PROGRESS__
```python
from goto_plus.Examples import goto-cal
```

## Contributing

1. Fork it ( https://github.com/ )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Make sure that the script does not have errors or warnings
6. Create a new Pull Request

## License

This tool is open source under the [MIT License](https://opensource.org/licenses/MIT) terms.

[[Back To Top]](#Python-GoTo)