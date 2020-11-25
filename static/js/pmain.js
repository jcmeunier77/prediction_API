const inputStrt = document.getElementById('strtinput')

const inputCity = document.getElementById('cityinput')

const encode3D = document.getElementById('encode3D')

const encodeMap = document.getElementById('encodeMap')


 encode3D.addEventListener('click', () => {

        // Invert the display state
        let street = inputStrt.value ;
        let city = inputCity.value ;
        let en3D = encode3D.value ;
        fetch("http://127.0.0.1:5000/3d/" + street + "/" + city + "/" + en3D).then(function(data)
        {
            console.log(data.json())
    // Here you get the data to modify as you please
    })
    })

encodeMap.addEventListener('click', () => {

        // Invert the display state
        let street1 = inputStrt.value ;
        let city1 = inputCity.value ;
        let enMap = encodeMap.value ;
        window.open("http://127.0.0.1:5000/map/" + street1 + "/" + city1 + "/" + enMap, "_blank");})

/*        fetch("http://127.0.0.1:5002/map/" + street1 + "/" + city1 + "/" + enMap).then(function(data)
        {
            console.log(data.json())
    // Here you get the data to modify as you please
    })
    })

 */