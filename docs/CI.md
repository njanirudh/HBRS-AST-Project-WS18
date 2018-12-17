### Adding Badges

* Badges can be added by :    
    * https://github.com/dwyl/repo-badges
    * https://shields.io/#/
    
* Depending on the git-hooks like CI , code refactoring app like 'codefactor' we can add badges that show the live build , code quality status on the README.md file.

* Other badges are simply markdown lines that are added to the readme file with specific status or values like build number , project status etc.
    
### Continuous Integration 

This project makes use of Travis for Continuous Integration (CI).    
The following [documentation](https://docs.travis-ci.com/user/tutorial/) explains the basic steps to add CI to the repository.
Depending on the lnguage of the project we can use the CI template.    

For our project we used python3 , specifically version 3.6.    
Since the project is not using any external dependencies , we dont require any 'requirements.txt'.       
The main.py and test_cases.py are inside the 'ast_project_2018' folder the changes are made in the script.

### Code Coverage 

This project is using [coveralls.io](https://coveralls.io) for code coverage test.
The application is directly run when travis runs all the default tests. 
