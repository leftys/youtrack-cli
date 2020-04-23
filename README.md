# Youtrack CLI

Command line interface for Youtrack designed to suit [Quantlane](http://quantlane.com/) workflow. 
Written for Python 2 because of official `youtrack` library incompatible with Python 3. This code is Python 3 compatible though.


## Set-up

```bash
pip install git+https://github.com/leftys/youtrack-cli.git
echo "export YOUTRACK_API_URL='https://your-youtrack-domain.com/'" >> ~/.profile
echo "export YOUTRACK_AUTH_TOKEN='get-this-in-your-youtrack-profile'" >> ~/.profile
```


## Examples

```bash
$ yt last --mine
 
PROJ-123 Task 1 summary
PROJ-120 Task 2 summary
(...)
```

```bash
$ yt issue RES 'Test task' -a some.assignee -r some.reviewer -u 'Some subproject' \
	-t 'Short term' -m MILE-123 -b 'My Agile Board'
$ yt done RES-123
$ yt reviewed RES-123
$ yt show RES-123
$ yt browse RES-123
$ yt command RES-123 'Any YouTrack command' 
$ yt --help
```

Usage together with bash aliases for filling usual projects/assignees/... is recommended!

```bash
echo "alias ytabc='yt issues ABC -a my.username -r reviewer -b 'My Agile Board' ...'" >> ~/.profile
```
