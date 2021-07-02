



# Neural-Network-Visualizer-Web-App
Web based visualization of neural network prediction using keras and streamlit. 

https://user-images.githubusercontent.com/86816817/124223015-84e57a00-db20-11eb-9784-28e8cf97187c.mp4
## Initial setup
1. Clone the repository: `git clone https://github.com/name-dhruv/Neural-Network-Visualiser.git`
2. `cd <repository-path>`
3. Install the python libraries: `pip install -r requirements.txt`

## Running the program
1. Train the model using `python train_model.py`.
2. Start the flask server using `python ml_server.py`.
3. While the flask server is running, in a new terminal run streamlit server using `streamlit run app.py`

## To push your changes-
1. Make sure you are in the new branch you created. You can check the current working branch using `git branch`.
2. `git add .`
3. `git commit -m "<commit-message>"`
4. `git push origin <branch-name>`
5. Create a pull request.

### If you ever install a new python library, make sure to run this command
`pip freeze > requirements.txt`
