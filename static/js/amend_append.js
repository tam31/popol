function append_row(e){

    console.log("추가기능")

    var div0 = document.createElement('div'); //div 만들기-->
//    div0.style.cssText = "display: flex; justify-content: center; align-items: center;"
    div0.className = 'div1'

    var div1 = document.createElement('div'); //div 만들기-->
//    div1.style.cssText = "box-shadow: rgb(31 38 135 / 15%) 0px 8px 32px 0px !important; background: rgba(255, 255, 255, 1) !important; border-radius: 4px !important; border-width: initial !important; border-style: none !important; border-color: initial !important; border-image: initial !important; margin: 4px !important; display: flex; align-items: center; flex-direction: row; padding: 8px; width: 300px; position: relative; touch-action: none; user-select: none;"
    div1.className = 'tour';    //div class
    div1.setAttribute("value", $(e).prev().text()); //div value
    console.log($(e).prev().text())

    //이미지
    var div2 = document.createElement('div');
//    div2.style.cssText = "position: relative;"
    div2.className='div2'
    var x = document.createElement("IMG");
//    x.setAttribute('width', '80px');
//    x.setAttribute('height', '65px');
//    x.setAttribute('object-fit', 'cover');
//    x.setAttribute('border-radius', '2px');
//    x.setAttribute('min-width', '65px');
    x.setAttribute("src", $(e).parent().prev().children().attr("src"));
    x.setAttribute("class", "check1");
//    console.log("이미지", x)
    div2.appendChild(x); //div 텍스트 적기
    div1.appendChild(div2);

    //관광지
    var div3 = document.createElement('div');
//    div3.style.cssText = "display: flex; flex-direction: column; text-align: left; justify-content: space-around;"
    div3.className="div3"
    var div4 = document.createElement('div'); //div 만들기-->
//    div4.style.cssText ="white-space: nowrap; text-overflow: ellipsis; overflow: hidden; max-width: 200px"
    div4.className="div4"
    div4.setAttribute('value', $(e).prev().text());
    const message2 = document.createTextNode($(e).prev().text());
    div4.appendChild(message2);
    div3.appendChild(div4);

    var div5 = document.createElement('div'); //div 만들기-->
    var but = document.createElement('button'); //button 만들기-->
    but.className="delete-link"
    const message3 = document.createTextNode("삭제");
    but.appendChild(message3);
    div5.appendChild(but);
    div3.appendChild(div5)

     //마커표시를 위해 위도 경도
    var div6 = document.createElement('div');
    div6.setAttribute("value", $(e).next().attr('value'))
    div6.setAttribute("class", "check2");
    div3.append(div6)

    var div7 = document.createElement('div');
    div7.setAttribute("value", $(e).next().next().attr('value'))
    div7.setAttribute("class", "check3");
    div3.append(div7)

    div1.appendChild(div3); //최종 div에 넣어 추가하기
    div0.appendChild(div1); //최종 div에 넣어 추가하기
//    console.log(div1)

    $(".Travel").append(div0);

    //마커추가하기
//    console.log("위도, 경도")
//    console.log($(e).next().attr("value"), $(e).next().next().attr("value"))

    var markerPosition  = new kakao.maps.LatLng($(e).next().attr("value"), $(e).next().next().attr("value"));
    var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35);
    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: markerPosition,
        title : $(e).prev().text(), // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage // 마커 이미지
    });

    //여기 수정
    var content = '<div class ="label"><span class="left"></span><span class="center">'+$(e).prev().text()+'</span><span class="right"></span></div>';
    var customOverlay = new kakao.maps.CustomOverlay({
        position: new kakao.maps.LatLng($(e).next().attr("value"), $(e).next().next().attr("value")),
        content: content
    });
    //이거 위에 이름 띄우는거
    customOverlay.setMap(map);
    writes.push(customOverlay)
    //여기까지

    // 마커에 표시할 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({
        content: $(e).prev().text() // 인포윈도우에 표시할 내용
    });
    console.log($(e).prev().text())
    // 마커에 mouseover 이벤트와 mouseout 이벤트를 등록합니다
    // 이벤트 리스너로는 클로저를 만들어 등록합니다
    // for문에서 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다
    kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
    kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));

//    console.log(marker)
    // 마커가 지도 위에 표시되도록 설정합니다
    marker.setMap(map);
    markers.push(marker);
//    console.log(markers)

    console.log("추가성공")
}
