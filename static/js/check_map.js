var markers=[] //카카오방식으로 위도경도이름을 찾기위해
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(35.1795543, 129.0756416), // 지도의 중심좌표
        level:9, // 지도의 확대 레벨
    };

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);
var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

var re = JSON.parse(JSON.parse(document.getElementById('check').textContent))

//console.log('re',re)
//[{{re | safe }}]

for (var i = 0; i < re.length; i ++) {

    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35);

    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    var content = '<div class ="label"><span class="left"></span><span class="center">'+re[i].name+'</span><span class="right"></span></div>';

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: new kakao.maps.LatLng(re[i].lat, re[i].lon), // 마커를 표시할 위치
        title : re[i].name, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage // 마커 이미지
    });

    var customOverlay = new kakao.maps.CustomOverlay({
        position: new kakao.maps.LatLng(re[i].lat, re[i].lon),
        content: content
    });
    // 커스텀 오버레이를 지도에 표시합니다
    customOverlay.setMap(map);
//    console.log(marker.n)//위도 경도
    markers.push(marker)
}
