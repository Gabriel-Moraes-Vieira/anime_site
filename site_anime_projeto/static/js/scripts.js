function ShowOrHide(){
    if (document.getElementById('genres-list').style.display == "none"){
    document.getElementById('genres-list').style.display = "block";
    document.getElementById('main').style.opacity = '0.5'
    } else{
        (document.getElementById('genres-list').style.display = "none")
        document.getElementById('main').style.opacity = '1'
    }
};

function AbrirNav(){
    document.getElementById("hidden-user-menu").style.height="250px";
    document.getElementById("hidden-user-menu").style.width="250px";
    document.getElementById("main").style.opacity="0.5"
    
    
};

function FecharNav() {
    document.getElementById("hidden-user-menu").style.width="0";
    document.getElementById("hidden-user-menu").style.height="0";
    document.getElementById("main").style.opacity="1"
};


