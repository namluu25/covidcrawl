document.getElementById("app").innerHTML = `
<h1>COVID 19 NEWS</h1>
${img.map(function(pet){
    return pet.caption
})}
`
