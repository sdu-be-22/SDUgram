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
    var fav_adver = document.getElementById('fav_adver');
    if (document.querySelectorAll(".row.m-4.card_c").length == 1) {
        document.getElementById('text').remove();
        const div = document.createElement('div');
        div.className = "row";
        const div_child = document.createElement('div');
        div.appendChild(div_child);
        div.className = "col-md-12";
        div_child.innerHTML = `<div class="div" style="text-align:center; padding: 30px 0 30px 0;">

                    <svg xmlns="http://www.w3.org/2000/svg" width="200" height="201" viewBox="0 0 200 201" >
                    <g fill="none" fill-rule="evenodd">
                        <path fill="#FFD5CD" d="M181.008 83.183a22.627 22.627 0 0 0 5.88-15.334c-.046-12.543-10.25-22.674-22.79-22.627-9.763.037-18.062 6.23-21.239 14.89-3.24-8.636-11.585-14.768-21.348-14.731-12.54.047-22.668 10.253-22.622 22.797.024 6.436 2.727 12.231 7.042 16.349h-.01l36.967 36.695s37.765-37.656 38.012-37.924l.11-.115h-.002zM61.147 56.198a14.23 14.23 0 0 0 3.742-9.685c-.03-7.922-6.523-14.32-14.504-14.29a14.45 14.45 0 0 0-13.515 9.403 14.45 14.45 0 0 0-13.585-9.304c-7.98.03-14.426 6.476-14.396 14.398.015 4.065 1.735 7.726 4.481 10.326h-.006L36.89 80.222S60.92 56.44 61.078 56.27l.07-.072h-.001z"/>
                        <path fill="#FFAA9A" d="M131.407 125.229a25.049 25.049 0 0 0 6.482-16.948c-.052-13.864-11.3-25.06-25.122-25.01-10.762.041-19.909 6.887-23.41 16.458-3.573-9.544-12.77-16.322-23.532-16.281-13.823.051-24.987 11.332-24.936 25.195.026 7.114 3.006 13.52 7.763 18.07h-.011l40.748 40.559s41.627-41.62 41.898-41.917l.122-.126h-.002z"/>
                        <path fill="#FF8169" d="M65.082 83.274c-14.705-.177-25.245 11.356-25.193 25.248.027 7.128 3.037 13.548 7.843 18.108h-.011l41.168 40.642S66.548 88.987 65.082 83.274z"/>
                        <path fill="#002F34" d="M143.273 94.222h6.42v-1.5h-4.188l4.152-5.796v-1.104h-6.264v1.5h4.008l-4.128 5.796zM155.24 91.318h3.337V89.83h-3.336zM164.089 94.222h6.42v-1.5h-4.188l4.152-5.796v-1.104h-6.264v1.5h4.008l-4.128 5.796zM176.057 91.318h3.336V89.83h-3.336zM184.905 94.222v-1.104l4.128-5.796h-4.008v-1.5h6.264v1.104l-4.152 5.796h4.188v1.5zM111.389 111.222a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7m0 2.693a.809.809 0 0 1 0 1.615.809.809 0 0 1 0-1.615M99.889 108.187h8v-4h-8zM113.889 108.187h8v-4h-8z"/>
                    </g>
                    </svg>
                    <h3>There are currently no favorite ads.</h3>
                    <p>You can bookmark an ad by clicking on the star in the listings or on the ads page.<br>Your favorite ads will be available on any device</p>
                    <p></p>
                </div> `;
         fav_adver.appendChild(div_child);
    }
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


function searchToggle(obj, evt){
    var container = $(obj).closest('.search-wrapper');
        if(!container.hasClass('active')){
            container.addClass('active');
            evt.preventDefault();
        }
        else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
            container.removeClass('active');
            // clear input
            container.find('.search-input').val('');
        }
}

$('#group input:checkbox').click(function(){
	if ($(this).is(':checked')) {
		 $('#group input:checkbox').not(this).prop('checked', false);
	}
});

$('input:checkbox').click(function(){
    console.log("value: " + $(this).val())
    update_ad($(this).val());
});

function update_ad(val) {
    $.ajax({
      method: "POST",
      url: "/by_city",
      data: {
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        'city': val,
      },
      success: function(data) {
        var mydata = JSON.parse(data);
        console.log(mydata);
        console.log(mydata.type) // check out how data is structured


//        // Update the coin amount
//        $('.status').contents()[0].textContent = 'Balance&nbsp'+data.coins
        var node = document.getElementById('obj');
        while (node.hasChildNodes()) {
            node.removeChild(node.lastChild);
        }
        for (let i = 0; i < mydata.length; i++) {
            const div = document.createElement('div');
            div.className = "row m-4 card_c " + mydata[i].pk;
            div.id = "row m-4 card_c " + mydata[i].pk;
            div.style = "padding:10px; background-color:white";
            var fav_img = "";
            if (mydata[i].fields)
            div.innerHTML = `
                <div class="col-md-3" style="max-width: 23%;">
                    <a href=/adver/${mydata[i].pk}/><img src="media/${mydata[i].fields.advertisement_image}" class="card-img-top" style="width: 16rem; height: 12rem;"></a>
                </div>
                <div class="col-md-7">
                    <a href=/adver/${mydata[i].pk}/ style="color:black;font-family:'Plus Jakarta Sans',sans-serif;"><h4>${mydata[i].fields.advertisement_name}</h4></a>
                    <p class="card-text" style="font-family: 'Mulish', sans-serif; serif;font-weight:bold;font-size:17px;">${mydata[i].fields.advertisement_location}, KAZAKHSTAN</p>
                    <p>${mydata[i].fields.advertisement_date_created}</p>
                </div>
                <div class="col-md-2" style="padding-right: 5px;">
                    <p class="card-text" style="float:right; font-size:20px;font-weight:bold; padding-left: 35px">${mydata[i].fields.advertisement_price} KZT</p>
                    <form method="POST" style="float:right;">
                        <input type="hidden" name="csrfmiddlewaretoken" value="IUPjN0BPaYtkBKeR8VT6Bol8jSl03yTYxCxmO5CmzUm8VQCYHMKNnIt3VBCjfzbB">
                        <button class="bt" onclick="postdata(this)" value=mydata[i].pk type="button" style="border:0; background:transparent;">
                            <img id="a"+mydata[i].pk src="/static/img/icons8-favorite-48.png" alt="">
                        </button>
                    </form>
                </div>
            `;
            console.log(div);
            document.getElementById('obj').appendChild(div);
        }


      }
    })
  };
