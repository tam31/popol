$("#sortTableForm").on("click", ".delete-link", function () {
        console.log("삭제성공입니다")

        // 아래 코드는 지도 위의 마커를 제거하는 코드입니다
        //console.log($(this).parent().attr('value')) //삭제 이름명
        //console.log(markers) //삭제 markers(여행일정순서)에 저장되어 있음 -> 삭제할때는 배열에 빼지 않아 배열안에는 저장되어 있음
        for(var i = 0 ; i < markers.length; i++){
            //console.log(markers[i].Gb) // 배열안에 있는 이름명
            if(markers[i].Gb ===$(this).parent().prev().attr('value')){
                console.log($(this).parent().prev().attr('value')) //삭제하고 싶은 이름
                let removed = markers[i].setMap(null)
                let remove2 = writes[i].setMap(null)
            }
        }

        $(this).parent().parent().parent().parent().remove();
});