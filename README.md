# Build jenkins job from Github Action :rocket:

This action builds/triggers a jenkins job, waiting it to be finished and enabling to pass job params.

## Inputs

### `jenkins-token`

**Required**
 
 ### `jenkins-url`

**Required** 

### `jenkins-user`

**Required** 

### `job-name`

**Required**

### `job-params`

**Not mandatory**

Set jenkins params as JSON string:  

E.g.
```
 "{'param1': 'value1', 'param2': 'value2'}"
``` 


## Example usage
```
    - name: "Trigger jenkins job"
      uses: GoldenspearLLC/build-jenkins-job@master
      with:
        jenkins-url: ${{ secrets.JENKINS_URL }}
        jenkins-token: ${{ secrets.JENKINS_TOKEN }}
        user: "jenkins-username"
        job-path: "job/folder_name/job/job_name"
        job-params: "{'param1': 'value1', 'param2': 'value2'}"
```
