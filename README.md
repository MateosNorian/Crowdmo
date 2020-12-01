<p align="center"><img src="https://i.ibb.co/7z2sJkd/crowdmo-logo.png" height="240px"></p>

# Crowdmo :money_with_wings:
Crowdmo is a web application that allows Venmo users to create crowdfunds. <br><br>
For example, imagine you wanted to pool together money for a fantasy football league, but you didn't want to go through the hassle of collecting cash from everyone, or individually Venmo requesting everyone and monitoring whether or not they had paid yet. <br><br>
Instead, you could create a crowdfund with Crowdmo. Using Crowdmo, you could specify a minimum league buy in, and a total cash goal for the crowdfund. After creating your crowdfund you could simply text the link to everyone in your league, and all they would have to do is type in their Venmo username and they would be auto-requested the the minimum contribution fee via Venmo. Once they pay the fee, the list of contributors is updated on the crowdfund page.<br><br> [Check out the project website here](https://mateosnorian.github.io/Crowdmo/). 

# Which tecnologies does this app use? :computer:
<table>
  <tbody>
    <tr valign="top">
      <td width="25%" align="center">
        <span><strong>HTML5</strong></span><br><br><br>
        <img height="64px" src="https://cdn.svgporn.com/logos/html-5.svg">
      </td>
      <td width="25%" align="center">
        <span><strong>CSS3</strong></span><br><br><br>
        <img height="64px" src="https://cdn.svgporn.com/logos/css-3.svg">
      </td>
    </tr>
    <tr valign="top">
      <td width="25%" align="center">
        <span><strong>Python</strong>
        </span><br><br><br>
        <img height="64px" src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-128.png">
      </td>
      <td width="25%" align="center">
        <span><strong>Flask</strong></span><br><br><br>
        <img height="64px" src="https://cdn.svgporn.com/logos/flask.svg">
      </td>
      <td width="25%" align="center">
        <span><strong>SQLite</strong></span><br><br><br>
        <img height="64px" src="https://cdn.svgporn.com/logos/sqlite.svg">
      </td>
    </tr>
    <tr valign="top">
      <td width="25%" align="center">
        <span><strong>Git</strong></span><br><br><br>
        <img height="64px" src="https://cdn.svgporn.com/logos/git-icon.svg">
      </td>
      <td width="25%" align="center">
        <span><strong>VS Code</strong></span><br><br><br>
        <img height="64px" src="https://cdn.svgporn.com/logos/visual-studio-code.svg">
      </td>
      <td width="25%" align="center">
        <span><strong>Heroku</strong></span><br><br><br>
        <img height="64px" src="https://cdn.svgporn.com/logos/heroku-icon.svg">
      </td>
    </tr>
  </tbody>
</table>

# How do I use this app? :grey_question:
1. To use Crowdmo, visit https://crowdmo.herokuapp.com, 
2. To create a crowdfund, navigate to https://crowdmo.herokuapp.com/create and fill out some info about your crowdfund.
3. Type in your Venmo username and password.
4. Input the 2FA code you receive on your phone.
5. Done! Send the link to some people and watch your crowdfund grow!

# Want to run Crowdmo on your local machine? :round_pushpin:
<strong>Please note, you must have [Python 3](https://www.python.org/downloads/) installed on your machine for these instructions to work</strong>
1. Install the code for this project
2. Navigate to the app.py file
3. Change ```app.secret_key = os.environ.get('SECRET_KEY', None)``` to ```app.secret_key = "testing"```
4. Save the file
5. Open the command prompt/terminal
6. Navigate to the directory the project was installed in
7. On Windows, run ```> py -3 -m venv venv``` on Mac, run ```$ python3 -m venv venv```
8. On Windows, run ```> venv\Scripts\Activate``` on Mac, run ```$ . venv/bin/activate```
9. Then install the necessary packages, ```pip install Flask Flask-SQLAlchemy requests```
8. Then, on Windows
```
> set FLASK_APP = app.py
> flask run
```
on Mac
```
$ export FLASK_APP = app.py
$ flask run
```
9. Navigate to ```127.0.0.1:5000/``` in the browswer
10. Have fun!

# Can I see a demo of the app? :video_camera:
[![Crowdmo Demo](http://img.youtube.com/vi/yT0J0RpvATk/0.jpg)](http://www.youtube.com/watch?v=yT0J0RpvATk "Crowdmo Demo")

# Attribution :fire:
This app uses the awesome [Venmo API Python Wrapper](https://github.com/mmohades/Venmo) created by [Mark Mohades](https://github.com/mmohades).

