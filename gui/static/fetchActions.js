function onFetchData(){
    let runValue =  getStringValueFromInputField("runInput");
    if (!runValue){
        showApiError("Empty RUN input value");
    }

    fetch("/fetch/" + runValue).then(
        (response) => {
            validateApiResponseCode(response);
            logs(response)
        }
    );
}

function deleteRun(run){
    fetch(run,{
        method:"DELETE"
    }).then(
        response => { 
            validateResponseCode(response);
            showApiMessage("Deleted " +response.text + "file")
        }
    )
};