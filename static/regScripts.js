function send()
{
    if (validace()){
        var data ={
        "jmeno": $("#name").val(),
        "plave": $("#plave").val(),
        "kamarad": $("#kamos").val(),
            "trida": $("#trida").val()
        };

        jQuery.ajax({
            type: "POST",
            url: '/restapi/odeslano',
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: 'json',
            success:function(data) {
                alert(data["processed"])
                document.getElementById("name").value = "";
                document.getElementById("kamos").value = "";
                document.getElementById("trida").value = "";
            }
        });
    }else {
        alert("spatne zapsane hodnoty")
    }
}

function validace(){
    plavec = $("#plave").val();
    name = $("#name").val();
    kamos = $("#kamos").val();
    trida = $("#trida").val();

    if (plavec == 0) {
        alert("Musis umet plavat sefe.");
        return false;
    }
    if (name.length < 2 || name.length > 20) {
        alert("Jmeno musi mit od 2 do 20 znaku.");
        return false;
    }
    if (trida.length < 0 || trida.length > 5) {
    alert("Invalidni trida.")
        return false;
    }
    if (kamos.length == 0){
        return true;
    }else {
        if (kamos.length >= 2 && kamos.length <= 20) {
            return true;
        }else{
            alert("Jmeno kamose musi mit od 2 do 20 znaku.");
            return false;
        }
    }

}
