# Youtrack CLI

Command line interface for Youtrack designed to suit [Quantlane](http://quantlane.com/) workflow. 
Written for Python 2 because of official `youtrack` library incompatible with Python 3. This code is Python 3 compatible
though.


# Set-up

```bash
pip install ssh+https://github.com/leftys/youtrack-cli.git
echo "export YOUTRACK_API_URL='https://youtrack.int.quantlane.com/'" >> ~/.profile
echo "export YOUTRACK_AUTH_TOKEN='...'" >> ~/.profile
```


## Examples

```bash
$ yt last --mine
 
PROJ-123 Task 1 summary
PROJ-120 Task 2 summary
(...)
```

```bash
$ yt issue RES 'Test task' -a some.assignee -r some.reviewer -u 'Some subproject' -t 'Short term' -m MILE-123
$ yt review RES-123
$ yt done RES-123
$ yt command RES-123 'Any YouTrack command' 
```

Usage together with bash aliases for filling usual projects/assignees/... is recommended!
