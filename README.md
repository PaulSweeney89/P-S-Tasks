# P-S-Tasks
Programming and Scripting Weekly Tasks

- Week 1: Set-up github & install software

- Week 2: BMI-Calc

- Week 3: secondstring

- Week 4: collatz

- Week 5: weekday

- Week 6: squareroot

- Week 7: es

[Learn Online Gmit](https://learnonline.gmit.ie/course/view.php?id=1598)

## GIT commands used for submodules
Weekly tasks were intially created as indivual repositories and were then included into this main repository as submodules.

- adding other repository as submodule.

```
git submodule add https://github.com/<user>/<repository> <repository_name>
```

- download contents of submodule into new repository.

```
git submodule update --init --recursive
```

- commit & push new repository with submodules to github.
``` 
git commit -m "<comment>"
git push
```
- to update all submodules within repository following individual updating of submodules. 
```
git submodule foreach git pull origin master
```

[Working with submodules](https://github.blog/2016-02-01-working-with-submodules/)





