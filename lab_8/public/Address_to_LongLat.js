async function toLongLat(address){
    var latlong
    try{
        const response = await fetch('https://api.opencagedata.com/geocode/v1/json?q='+address+'&key=b0fd253b4b84485994275fdad6860620')
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        const json = await response.json()
        console.log(json)
        if(json.status.code = 200){
            latlong = json.results[0].geometry
            console.log(latlong)
            return(latlong)
        }else{
            latlong = "Unable to locate address."
            return(latlong)
        }
    }catch(error){
        console.log('There has been a problem with your fetch operation: ', error.message);
        latlong = 'There has been a problem with your fetch operation: ', error.message
        return(latlong)
    }
}
