const getCharacterData = () => {
    return new Promise(function(resolve,reject){
        const error = true;
        if(!error){
            setTimeout[resolve({id:1, name:'Prajwal'}), 1000];
        }
        else{
            return reject('Alright');
        }

    }
    
    )
}

getCharacterData()
.then(response=>console.log(response))
.catch(error=>console.log(error));
