function like(pk) {
    var element=document.getElementById("like")
    var count=document.getElementById("count")
    $.get(`/like/${pk}`).then(Response => {
        if(Response['response'] === "liked"){
            element.className = "fa-solid fa-heart fa-lg text-danger"
            count.innerText = Number(count.innerText) +1
        }
        else{
            element.className = "fa-regular fa-heart fa-lg"
            count.innerText = Number(count.innerText) -1
        }
    })
}

function bookmark(pk) {
    var element=document.getElementById("bookmark")
    var count=document.getElementById("count")
    $.get(`/bookmark/${pk}`).then(Response => {
        if(Response['response'] === "saved"){
            element.className = "fa-solid fa-bookmark fa-lg me-1"
            count.innerText = Number(count.innerText) +1
        }else{
            element.className = "fa-regular fa-bookmark fa-lg me-1"
            count.innerText = Number(count.innerText) -1
        }
    })
}
