function newta(e) { //길 상세보기
//    console.log("클릭",$(e).attr('id'))
//    console.log(markers)
    var num = parseInt($(e).attr('id'))

//    console.log(re[num])//네이버 방식
    //네이버방식
//    console.log(re[num].name, re[num+1].name); //네이버방식
<!--        var end= 'http://map.naver.com/index.nhn?slng='+re[num].lon+'&slat='+re[num].lat+'&stext='+re[num].name+'&elng='+re[num+1].lon+'&elat='+re[num+1].lat+'&etext='+re[num+1].name+'&menu=route&pathType=1'-->

    //카카오방식
//    console.log(markers[num].Gb, markers[num].n.La, markers[num].n.Ma)//카카오방식
    var end='https://map.kakao.com/?sX='+markers[num].n.La+'&sY='+markers[num].n.Ma+'&sName='+markers[num].Gb+'&eX='+markers[num+1].n.La+'&eY='+markers[num+1].n.Ma+'&eName='+markers[num+1].Gb
    window.open(end)
}

var re = JSON.parse(JSON.parse(document.getElementById('check').textContent))
var day = 1
//console.log(re);
for(var i = 0 ; i<re.length ; i++){
    var div1 = document.createElement('div'); //div 만들기-->
//    div1.style.cssText = "border:1px solid; padding:5px; width:320px; hight:300px; display: flex; flex-direction: column;";   //div style
    div1.className = 'div1'   //div class
    div1.setAttribute("value", re[i].name)
//    if(i!==re.length-1){
//        console.log(re[i].name, re[i+1].name)
//    }

    //일차별
    var div2 = document.createElement('div');
//    div2.style.cssText = "border:1px solid; width:50px;"
    div2.className="daytime"
    const messageTime = document.createTextNode(day+'일차');
    div2.appendChild(messageTime);
    div1.appendChild(div2);
    //일차증가하기
    if(re[i].name.search("호텔|모텔") > -1){ //숙소인경우 하루 증가
//        console.log("데이")
        day += 1
//        console.log(day)
    }

    var div3 = document.createElement('div'); //div 만들기-->
    div3.className = 'check';
     //이미지
    var div4 = document.createElement('div');
//    div2.style.cssText = "border:1px solid; width:100px; float: left"
    div4.className="div2"
    var x = document.createElement("IMG");
//    x.setAttribute('width', '100px');
    x.className="checkImg"
    x.setAttribute("src", re[i].url);
    div4.appendChild(x); //
    div3.appendChild(div4);

    //이름
    var div5 = document.createElement('div');
//    div3.style.cssText = "height: 30%; width:300px; margin: 0 auto; flex-grow: 1;"
    div5.className = "div3"

    var div6 = document.createElement('div');
    div6.className="div4"
    const message2 = document.createTextNode(re[i].name);
    div6.appendChild(message2);
    div5.appendChild(div6)
    div3.appendChild(div5);

     if(i!==re.length-1){
//        console.log("여기",i)
        var div7 = document.createElement('div');
        div7.className='div5'
        div7.setAttribute('onClick', 'newta(this)');
        div7.setAttribute('id', i);


        var div8 = document.createElement('div');
//        div8.setAttribute('type', 'button');
//        div8.setAttribute('onClick', 'newta(this)');
//        div8.setAttribute('value', '경로보기');
//        div8.setAttribute('id', i);
        div8.setAttribute('class', 'chck5');
        const message3 = document.createTextNode("경로 보기");
        div8.appendChild(message3)

//        console.log(div4)
        div7.appendChild(div8)
        div3.appendChild(div7);
    }
    div1.appendChild(div3)

//    console.log(re[i].lat, re[i].lon)
    $(".check1").append(div1);
}
