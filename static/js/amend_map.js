var markers = [];
var writes = [];
//console.log("지도표시")
//console.log("plan1", plans1) //객체표시
var mapContainer = document.getElementById('map'), // 지도를 표시할 div

mapOption = {
    center: new kakao.maps.LatLng(35.1795543, 129.0756416), // 지도의 중심좌표
    level:9 // 지도의 확대 레벨
};

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

let plans = JSON.parse(document.getElementById('plans1').textContent) // JSON 양식 문자열 이기 때문에 JSON.parse 함수를 이용해 다시 JSON 객체 바꿔줌

//console.log("plans", plans) //객체표시
for (var i = 0; i < plans.length; i ++) {
    // 마커 이미지의 이미지 크기 입니다
        var imageSize = new kakao.maps.Size(24, 35);

        // 마커 이미지를 생성합니다
        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({
            map: map, // 마커를 표시할 지도
            position: new kakao.maps.LatLng(plans[i].Latitude, plans[i].Lognitude),
            title : plans[i].name, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
            image : markerImage // 마커 이미지
        });
        marker.setMap(map);
        markers.push(marker)
        // 마커에 표시할 인포윈도우를 생성합니다
        var infowindow = new kakao.maps.InfoWindow({
            content: plans[i].name // 인포윈도우에 표시할 내용
        });

        kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));


        var content = '<div class ="label"><span class="left"></span><span class="center">'+plans[i].name+'</span><span class="right"></span></div>';
        var customOverlay = new kakao.maps.CustomOverlay({
            position: new kakao.maps.LatLng(plans[i].Latitude, plans[i].Lognitude),
            content: content
        });
        // 커스텀 오버레이를 지도에 표시합니다
        customOverlay.setMap(map);
        writes.push(customOverlay)
}

//console.log(markers[0].Gb)
//console.log(markers.length)
function makeOverListener(map, marker, infowindow) {
    return function() {
        infowindow.open(map, marker);
    };
}

// 인포윈도우를 닫는 클로저를 만드는 함수입니다
function makeOutListener(infowindow) {
    return function() {
        infowindow.close();
    };
}

