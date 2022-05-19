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

document.getElementById('form-select').addEventListener('change', function() {
  val = $( "#form-select" ).val();

  console.log(val)
  if(val === '1') {
    window.location.replace('/today','_blank');
    }
  if(val === '2') {
    window.location.replace('/oder_by_date', '_blank');
  }
  if (val === '3') {
    window.location.replace('/price_max', '_blank');
  }
  if (val === '4') {
    window.location.replace('/price_min', '_blank')
  }
});


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
        ''
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
            div.style = "padding:10px; background-color:#C8F8F6";
            var fav_img = "";
            if (mydata[i].fields)
            div.innerHTML = `
                <div class="col-md-3">
                    <a href=/adver/${mydata[i].pk}/><img src="media/${mydata[i].fields.advertisement_image}" class="card-img-top" style="width: 16rem; height: 14rem;border:solid 8px #FAE6B1;"></a>
                </div>
                <div class="col-md-7 pl-5">
                    <a href=/adver/${mydata[i].pk}/ style="color:black;font-family:'Plus Jakarta Sans',sans-serif;"><h4>${mydata[i].fields.advertisement_name}</h4></a>
                    <p class="card-text" style="font-family: 'Mulish', sans-serif; serif;font-weight:bold;font-size:17px;">${mydata[i].fields.advertisement_location}, KAZAKHSTAN</p>
                    <p>${mydata[i].fields.advertisement_date_created}</p>
                </div>
                <div class="col-md-2">
                    <p class="card-text" style="font-size:20px;font-weight:bold;">${mydata[i].fields.advertisement_price} KZT</p>
                    <form method="POST">
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
  $(document).ready(function() {

	$(".button a span").click(function() {
		var btn = $(this).parent().parent();
		var loadSVG = btn.children("a").children(".load");
		var loadBar = btn.children("div").children("span");
		var checkSVG = btn.children("a").children(".check");

		btn.children("a").children("span").fadeOut(200, function() {
			btn.children("a").animate({
				width: 56
			}, 100, function() {
				loadSVG.fadeIn(300);
				btn.animate({
					width: 320
				}, 200, function() {
					btn.children("div").fadeIn(200, function() {
						loadBar.animate({
							width: "100%"
						}, 2000, function() {
							loadSVG.fadeOut(200, function() {
								checkSVG.fadeIn(200, function() {
									setTimeout(function() {
										btn.children("div").fadeOut(200, function() {
											loadBar.width(0);
											checkSVG.fadeOut(200, function() {
												btn.children("a").animate({
													width: 150
												});
												btn.animate({
													width: 150
												}, 300, function() {
													btn.children("a").children("span").fadeIn(200);
												});
											});
										});
									}, 2000);
								});
							});
						});
					});
				});
			});
		});

	});

});


