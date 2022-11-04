jQuery(document).ready(function() {

    // sortable은 객체의 순서를 재배치 할 수 있다.
    jQuery(".Travel").sortable();
});

function wujuSonyeoTransmit() {
    console.log("보내기")
    var total = [];
   // tour의 개수만큼 반복문을 돌리면서 enName값을 콤마로 구분하여 하나의 문자열로 만든다.
    jQuery(".tour").each(function(idx) {
        //console.log(idx,jQuery(".tour").eq(idx).attr("value"), $(".check1").eq(idx).attr("src")) // 각 이름과 이미지, 위도경도
        // 한글 이름을 전송
        //total += jQuery(".tour.aa").eq(idx).text + ", ";

        //json형태로 넣기
        var check5 = JSON.stringify({
            'name': jQuery(".tour").eq(idx).attr("value"),
            'url' : $(".check1").eq(idx).attr("src"),
            'lat' : $(".check2").eq(idx).attr("value"),
            'lon' : $(".check3").eq(idx).attr("value")
        });
        //console.log(check5)
        //배열로 넣기 eq(idx)가 인덱스, attr는 그 인덱스의 속성
        total.push(check5)

        // 영문 이름을 전송
        //total += jQuery(".tour").eq(idx).attr("value") + ",";
    });


//    jQuery("#result").val(total); 원래는 이거였지만 []이 안들어가 밑에서 넣어줌

    jQuery("#result").val('[');
    $("#result").val( $("#result").val() + total );
    $("#result").val( $("#result").val() + "]" );
//    console.log(total)
//    console.log($("#result").val())
    $("#sortTableForm").attr("method", "post");
<!--        console.log($("#sortTableForm").attr('method'))-->
//    console.log("여기까지")
    $("#sortTableForm").submit();
}