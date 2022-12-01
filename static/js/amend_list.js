let dyndata1 = JSON.parse(document.getElementById('dyndata1').textContent)
let posts1 = JSON.parse(JSON.parse(document.getElementById('posts_js1').textContent))
let eats = JSON.parse(JSON.parse(document.getElementById('eats_js1').textContent))
let stays = JSON.parse(JSON.parse(document.getElementById('stays_js1').textContent))
var final = posts1.concat(eats,stays); //json array(객체형태)합치기

//console.log(posts1)
//console.log('ex',JSON.parse(document.getElementById('posts_js1').textContent))
auto =[]
for(var i = 0; i<final.length ; i++){
    auto.push(final[i].name)
}

//자동완성
$(function () {	//화면 로딩후 시작
    $("#search").autocomplete({  //오토 컴플릿트 시작
        source: auto,	//  List 배열
        focus : function(event, ui) { // 방향키로 자동완성단어 선택 가능하게 만들어줌
            return false;
        },
        minLength: 1,// 최소 글자수
        delay: 10,	//autocomplete 딜레이 시간(ms)
        //disabled: true, //자동완성 기능 끄기
    });
});

//검색
function searchBtn(){
    if($(".search").children().length>0){ //자식노드 삭제
        $(".search").empty();
    }

    const searchInput = $("#search").val();
//    console.log("검색")
//    console.log(searchInput) //검색한 값


    var ex = final.filter(function(e){  //객체이름과 텍스트 이름 비교
        return e.name === searchInput
    });

    if(ex.length>0){
        console.log(ex[0].name)
        var div1 = document.createElement('div'); //div 만들기-->
        div1.style.cssText = "box-shadow: rgb(31 38 135 / 15%) 0px 8px 32px 0px !important; background: rgba(255, 255, 255, 1) !important; border-radius: 4px !important; border-width: initial !important; border-style: none !important; border-color: initial !important; border-image: initial !important; margin: 4px !important; display: flex; align-items: center; flex-direction: row; padding: 8px; position: relative; touch-action: none; user-select: none;"
        div1.className = 'sear';    //div class
//        div1.className="tour"
        div1.setAttribute("value", ex[0].name); //div value

        //이미지
        var div2 = document.createElement('div');
//        div2.style.cssText = "position: relative;"
        div2.className="div2"
        var x = document.createElement("IMG");
//        x.setAttribute('width', '80px');
//        x.setAttribute('height', '65px');
//        x.setAttribute('object-fit', 'cover');
//        x.setAttribute('border-radius', '2px');
//        x.setAttribute('min-width', '65px');
        x.setAttribute("src", ex[0].url);
        x.setAttribute("class", 'check1');
        div2.appendChild(x); //div 텍스트 적기
        div1.appendChild(div2);

        var div3 = document.createElement('div');
//        div3.style.cssText = "display: flex; flex-direction: column; text-align: left; justify-content: space-around;"
        div3.className="div3"
        var div4 = document.createElement('div'); //div 만들기-->
//        div4.style.cssText ="white-space: nowrap; text-overflow: ellipsis; overflow: hidden; max-width: 200px"
        div4.className="div4"
        div4.setAttribute('value', ex[0].name);
        const message2 = document.createTextNode(ex[0].name);
        div4.appendChild(message2);
        div3.appendChild(div4);

        var but = document.createElement('button');
        but.setAttribute("type", "button");
        but.setAttribute("onClick", "append_row(this)");
//        but.style.cssText = "font-family: 'Material Icons'"
        but.className="butappend"
        const message3 = document.createTextNode("추가");
        but.appendChild(message3);
        div3.appendChild(but);

        //마커표시를 위해
        var div6 = document.createElement('div');
        div6.setAttribute("value", ex[0].Latitude)
        div3.append(div6)

        var div7 = document.createElement('div');
        div7.setAttribute("value", ex[0].Longitude)
        div3.append(div7)

        div1.appendChild(div3);


        $(".search").append(div1);

    }
    else{
        var div1 = document.createElement('div'); //div 만들기-->
//        div1.style.cssText = "box-shadow: rgb(31 38 135 / 15%) 0px 8px 32px 0px !important; background: rgba(255, 255, 255, 1) !important; border-radius: 4px !important; border-width: initial !important; border-style: none !important; border-color: initial !important; border-image: initial !important; margin: 4px !important; display: flex; align-items: center; flex-direction: row; padding: 8px; width: 300px; position: relative; touch-action: none; user-select: none;"
        div1.className="tour"
        const message3 = document.createTextNode("해당정보가 없습니다");
        div1.appendChild(message3);
        $(".search").append(div1);
    }
}

function plan_tour(){//관광지 리스트
    //console.log("관광지")
    let posts = dyndata1

    //console.log($(".container").children().length) //자식노드 수
    if($(".container").children().length>0){ //자식노드 삭제
       $(".container").empty();
    }
    for (var i = 0; i < posts.length; i++) { // 배열 arr의 모든 요소의 인덱스(index)를 출력함.
        var div1 = document.createElement('div'); //div 만들기-->
        div1.style.cssText = "box-shadow: rgb(31 38 135 / 15%) 0px 8px 32px 0px !important; background: rgba(255, 255, 255, 1) !important; border-radius: 4px !important; border-width: initial !important; border-style: none !important; border-color: initial !important; border-image: initial !important; margin: 4px !important; display: flex; align-items: center; flex-direction: row; padding: 8px; position: relative; touch-action: none; user-select: none;"
        div1.className = 'tour2';    //div class
        div1.setAttribute("value", posts[i].name); //div value


         //이미지
        var div2 = document.createElement('div'); //div 만들기-->
//        div2.style.cssText = "position: relative;"
        div2.className="div2"
        var x = document.createElement("IMG");
//        x.setAttribute('width', '80px');
//        x.setAttribute('height', '65px');
//        x.setAttribute('object-fit', 'cover');
//        x.setAttribute('border-radius', '2px');
//        x.setAttribute('min-width', '65px');
        x.setAttribute("src", posts[i].url);
        x.setAttribute("class", 'check1');
        div2.appendChild(x); //div 텍스트 적기
        div1.appendChild(div2);

        var div3 = document.createElement('div'); //div 만들기-->
//        div3.style.cssText = "display: flex; flex-direction: column; text-align: left; justify-content: space-around;"
        div3.className="div3"
        var div4 = document.createElement('div'); //div 만들기-->
//        div4.style.cssText ="white-space: nowrap; text-overflow: ellipsis; overflow: hidden; max-width: 200px"
        div4.className="div4"
        div4.setAttribute('value', posts[i].name);
        const message2 = document.createTextNode(posts[i].name);
        div4.appendChild(message2);
        div3.appendChild(div4);
//        div1.appendChild(div3);

        var but = document.createElement('button');
        but.setAttribute("type", "button");
        but.setAttribute("onClick", "append_row(this)");
//        but.style.cssText="width:50px"
        but.className="butappend"
        const message3 = document.createTextNode("추가");
        but.appendChild(message3);
        div3.appendChild(but);

         //마커표시를 위해
        var div6 = document.createElement('div');
        div6.setAttribute("value", posts[i].lat) //위도
        div3.append(div6)

        var div7 = document.createElement('div');
        div7.setAttribute("value", posts[i].lon) //경도
        div3.append(div7)

        div1.appendChild(div3); //마커
<!--                    console.log("마커")-->
<!--                    console.log(div1)-->

        $(".container").append(div1);
    }

}

function plan_res(){//식당 리스트
//    console.log("식당")
//    console.log($(".container").children().length) //자식노드 수
    if($(".container").children().length>0){ //자식노드 삭제
       $(".container").empty();
    }



    for (var i = 0; i < eats.length; i++) { // 배열 arr의 모든 요소의 인덱스(index)를 출력함.
        var div1 = document.createElement('div'); //div 만들기-->
        div1.style.cssText = "box-shadow: rgb(31 38 135 / 15%) 0px 8px 32px 0px !important; background: rgba(255, 255, 255, 1) !important; border-radius: 4px !important; border-width: initial !important; border-style: none !important; border-color: initial !important; border-image: initial !important; margin: 4px !important; display: flex; align-items: center; flex-direction: row; padding: 8px; position: relative; touch-action: none; user-select: none;"   //div style
        div1.className = 'eat2';    //div class
//        div1.className="tour"
        div1.setAttribute("value", eats[i].name); //div value

         //이미지
        var div2 = document.createElement('div');
//        div2.style.cssText = "position: relative;"
        div2.className="div2"
        var x = document.createElement("IMG");
//        x.setAttribute('width', '80px');
//        x.setAttribute('height', '65px');
//        x.setAttribute('object-fit', 'cover');
//        x.setAttribute('border-radius', '2px');
//        x.setAttribute('min-width', '65px');
        x.setAttribute("src", eats[i].url);
        x.setAttribute("class", 'check1');
        div2.appendChild(x); //div 텍스트 적기
        div1.appendChild(div2);

        var div3 = document.createElement('div');
//        div3.style.cssText = "display: flex; flex-direction: column; text-align: left; justify-content: space-around;"
        div3.className="div3"
        var div4 = document.createElement('div'); //div 만들기-->
//        div4.style.cssText ="white-space: nowrap; text-overflow: ellipsis; overflow: hidden; max-width: 200px"
        div4.className="div4"
        div4.setAttribute('value', eats[i].name);
        const message2 = document.createTextNode(eats[i].name);
        div4.appendChild(message2);
        div3.appendChild(div4);

        var but = document.createElement('button');
        but.setAttribute("type", "button");
        but.setAttribute("onClick", "append_row(this)");
        but.className="butappend"
        const message3 = document.createTextNode("추가");
        but.appendChild(message3);
        div3.appendChild(but);

        //마커표시를 위해
        var div6 = document.createElement('div');
        div6.setAttribute("value", eats[i].Latitude)
        div3.append(div6)

        var div7 = document.createElement('div');
        div7.setAttribute("value", eats[i].Longitude)
        div3.append(div7)

        div1.appendChild(div3);


        $(".container").append(div1);
    }

}

function plan_stay(){ //숙소 리스트
//    console.log("숙소")
//    console.log($(".container").children().length) //자식노드 수
    if($(".container").children().length>0){ //자식노드 삭제
       $(".container").empty();
    }


    for (var i = 0; i < stays.length; i++) { // 배열 arr의 모든 요소의 인덱스(index)를 출력함.
        var div1 = document.createElement('div'); //div 만들기-->
        div1.style.cssText = "box-shadow: rgb(31 38 135 / 15%) 0px 8px 32px 0px !important; background: rgba(255, 255, 255, 1) !important; border-radius: 4px !important; border-width: initial !important; border-style: none !important; border-color: initial !important; border-image: initial !important; margin: 4px !important; display: flex; align-items: center; flex-direction: row; padding: 8px; position: relative; touch-action: none; user-select: none;"//div style
        div1.className = 'stay2';    //div class
        div1.setAttribute("value", stays[i].name); //div value
        //이미지
        var div2 = document.createElement('div');
//        div2.style.cssText = "position: relative;"
        div2.className = "div2"
        var x = document.createElement("IMG");
//        x.setAttribute('width', '80px');
//        x.setAttribute('height', '65px');
//        x.setAttribute('object-fit', 'cover');
//        x.setAttribute('border-radius', '2px');
//        x.setAttribute('min-width', '65px');
        x.setAttribute("src", stays[i].url);
        x.setAttribute("class", 'check1');
        div2.appendChild(x); //div 텍스트 적기
        div1.appendChild(div2);

        var div3 = document.createElement('div');
//        div3.style.cssText = "display: flex; flex-direction: column; text-align: left; justify-content: space-around;"
        div3.className="div3"
        var div4 = document.createElement('div'); //div 만들기-->
//        div4.style.cssText ="white-space: nowrap; text-overflow: ellipsis; overflow: hidden; max-width: 200px"
        div4.className="div4"
        div4.setAttribute('value', stays[i].name);
        const message2 = document.createTextNode(stays[i].name);
        div4.appendChild(message2);
        div3.appendChild(div4);

        var but = document.createElement('button');
        but.setAttribute("type", "button");
        but.setAttribute("onClick", "append_row(this)");
        but.className="butappend"
        const message3 = document.createTextNode("추가");
        but.appendChild(message3);
        div3.appendChild(but);

         //마커표시를 위해 위도 경도
        var div6 = document.createElement('div');
        div6.setAttribute("value", stays[i].Latitude)
        div3.append(div6)

        var div7 = document.createElement('div');
        div7.setAttribute("value", stays[i].Longitude)
        div3.append(div7)

        div1.appendChild(div3);


        $(".container").append(div1);
    }
}