// $(document).ready(function () {
//     animateDiv($('.a'));


// });

// function makeNewPosition($container) {

//     // Get viewport dimensions (remove the dimension of the div)
//     var h = $container.height();
//     var w = $container.width();

//     var nh = Math.floor(Math.random() * h * Math.random());
//     var nw = Math.floor(Math.random() * w * Math.random());

//     return [nh, nw];

// }



// function animateDiv($target) {

//     var min = -20;
//     var max = 60;
//     // and the formula is:
//     var random = Math.floor(Math.random() * (max - min + 1)) + min;

//     var newq = makeNewPosition($target.parent());
//     var oldq = $target.offset();
//     var speed = calcSpeed([oldq.top, oldq.left], newq);

//     $target.animate({
//         top: newq[0],
//         left: newq[1] + random
//     }, speed, function () {
//         animateDiv($target);
//     });

// };

// function calcSpeed(prev, next) {

//     var x = Math.abs(prev[1] - next[1]);
//     var y = Math.abs(prev[0] - next[0]);

//     var greatest = x > y ? x : y;

//     var min1 = 1;
//     var max1 = 2;
//     var random1 = Math.floor(Math.random() * (max1 - min1 + 1)) + min1;
//     var speedModifier = 0.5 * random1;

//     var speed = Math.ceil(greatest / speedModifier);

//     return speed;

// }




// test
// test
// test
// test
// test
// test
// test
// test


$(document).ready(function () {
    animateDiv($('.a'));


});


function makeNewPosition() {

    // Get viewport dimensions (remove the dimension of the div)
    tgh = $(window).height();
    tgw = $(window).width();
    // console.log(tgh)
    // console.log(tgw)
    // 367
    // 1396
    // 562
    // 1745
    // tgh = 367;
    // tgw = 1396;
    // tgh = 562;
    // tgw = 1745;

    var min = 1;
    var max = 26;
    var random = Math.floor(Math.random() * (max - min + 1)) + min;
    console.log(random);

    if (random == 1) {
        var t1 = Math.floor(tgh * 0.06);
        var l1 = Math.floor(tgh * -0.25);
    } else if (random == 2) {
        var t1 = Math.floor(tgh * -0.025);
        var l1 = Math.floor(tgh * -0.13);
    } else if (random == 3) {
        var t1 = Math.floor(tgh * -0.09);
        var l1 = Math.floor(tgh * -0.002);
    } else if (random == 4) {
        var t1 = Math.floor(tgh * -0.13);
        var l1 = Math.floor(tgh * 0.15);
    } else if (random == 5) {
        var t1 = Math.floor(tgh * -0.15);
        var l1 = Math.floor(tgh * 0.3);
    } else if (random == 6) {
        var t1 = Math.floor(tgh * -0.16);
        var l1 = Math.floor(tgh * 0.45);
    } else if (random == 7) {
        var t1 = Math.floor(tgh * -0.16);
        var l1 = Math.floor(tgh * 0.59);

    } else if (random == 8) {
        var t1 = Math.floor(tgh * -0.155);
        var l1 = Math.floor(tgh * 0.745);
    } else if (random == 9) {
        var t1 = Math.floor(tgh * -0.15);
        var l1 = Math.floor(tgh * 0.87);


    } else if (random == 10) {
        var t1 = Math.floor(tgh * -0.135);
        var l1 = Math.floor(tgh * 0.96);
    } else if (random == 11) {
        var t1 = Math.floor(tgh * -0.115);
        var l1 = Math.floor(tgh * 1.1);
    } else if (random == 12) {
        var t1 = Math.floor(tgh * -0.05);
        var l1 = Math.floor(tgh * 1.225);
    } else if (random == 13) {
        var t1 = Math.floor(tgh * 0.0154);
        var l1 = Math.floor(tgh * 1.372);
    } else if (random == 14) {
        var t1 = Math.floor(tgh * 0.27);
        var l1 = Math.floor(tgh * -0.25);
    } else if (random == 15) {
        var t1 = Math.floor(tgh * 0.17);
        var l1 = Math.floor(tgh * -0.1);
    } else if (random == 16) {
        var t1 = Math.floor(tgh * 0.1);
        var l1 = Math.floor(tgh * 0.025);
    } else if (random == 17) {
        var t1 = Math.floor(tgh * 0.08);
        var l1 = Math.floor(tgh * 0.17);
    } else if (random == 18) {
        var t1 = Math.floor(tgh * 0.04);
        var l1 = Math.floor(tgh * 0.34);
    } else if (random == 19) {
        var t1 = Math.floor(tgh * 0.04);
        var l1 = Math.floor(tgh * 0.47);
    } else if (random == 20) {
        var t1 = Math.floor(tgh * 0.04);
        var l1 = Math.floor(tgh * 0.6);
    } else if (random == 21) {
        var t1 = Math.floor(tgh * 0.04);
        var l1 = Math.floor(tgh * 0.72);
    } else if (random == 22) {
        var t1 = Math.floor(tgh * 0.03);
        var l1 = Math.floor(tgh * 0.85);
    } else if (random == 23) {
        var t1 = Math.floor(tgh * 0.07);
        var l1 = Math.floor(tgh * 1);
    } else if (random == 24) {
        var t1 = Math.floor(tgh * 0.121);
        var l1 = Math.floor(tgh * 1.15);
    } else if (random == 25) {
        var t1 = Math.floor(tgh * 0.168);
        var l1 = Math.floor(tgh * 1.27);
    } else if (random == 26) {
        var t1 = Math.floor(tgh * 0.24);
        var l1 = Math.floor(tgh * 1.4);
    } else {
        var t1 = Math.floor(tgh * 0.5);
        var l1 = Math.floor(tgh * 0.5);


    }
    return [t1, l1];
}


function animateDiv($target) {

    var newq = makeNewPosition();
    var oldq = $target.offset();
    var speed = calcSpeed([oldq.top, oldq.left], newq);

    $target.animate({
        top: newq[0],
        left: newq[1]
    }, speed, function () {
        animateDiv($target);
    });

};

function calcSpeed(prev, next) {

    var x = Math.abs(prev[1] - next[1]);
    var y = Math.abs(prev[0] - next[0]);

    var greatest = x > y ? x : y;

    var speedModifier = 0.2;

    var speed = Math.ceil(greatest / speedModifier);

    return speed;

}

// test
// test
// test
// test
// test
// test
// test
// test









function showhide() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}