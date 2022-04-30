function postdata(link){
    var elem = document.getElementById("a" + $(link).val());
    if (elem.src === "http://127.0.0.1:8000/static/img/icons8-favorite-48.png") {
        elem.src = "/static/img/icons8-favorite-50.png";
    } else {
        elem.src = "/static/img/icons8-favorite-48.png";
    }
    $.ajax({
        type: "POST",
        url: "/add_favorite/",
        data:{
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'id': $(link).val(),
        },
        datatype:'json',
        success: function(data) {
        if (data['success'])
            alert("successfully added to favorites")
        }
    });
}
function remove_elm(link){
    var elem = document.getElementById("a" + $(link).val());
    if (elem.src === "http://127.0.0.1:8000/static/img/icons8-favorite-48.png") {
        elem.src = "/static/img/icons8-favorite-50.png";
    } else {
        elem.src = "/static/img/icons8-favorite-48.png";
    }
    $.ajax({
        type: "POST",
        url: "/add_favorite/",
        data:{
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'id': $(link).val(),
        },
        datatype:'json',
        success: function(data) {
        if (data['success'])
            alert("successfully added to favorites")
        }
    });
    var card = document.getElementById("row m-4 card_c " + $(link).val());
    let id = null;
    let pos = 0;
    clearInterval(id);
    id = setInterval(frame, 0.1);

    function frame() {
        if (pos < -1200) {
            clearInterval(id);
            card.remove();
        } else {
            pos-=20;
            card.style = "padding:10px; background-color:#B3DEE5;" +  'transform:translateX(' + pos + 'px' +  ')';
        }
    }
}
