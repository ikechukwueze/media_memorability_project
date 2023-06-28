
//document.getElementById("uploadForm").addEventListener('submit', uploadVideo)
$("#uploadForm").bind('submit', uploadVideo)

//document.getElementsByClassName("btn-close")[0].addEventListener('click', hideModal)
$(".btn-close").bind('click', hideModal)

//document.getElementById("video").addEventListener('change', getFileSize)
$("#video").bind('change', getFileSize)

var file_size

function getFileSize(e) {
    //this.files[0].size gets the size of your file.
    file_size = this.files[0].size / 1024;
};



function hideModal(e) {
    $('#exampleModal').modal('hide')
}


async function uploadVideo(e) {
    e.preventDefault()
    // insert spinner in modal content
    $("#video_score").replaceWith("<div class='spinner-border' role='status' id='video_score'><span class='sr-only'></span></div>");


    let csrf = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="))
        ?.split("=")[1];

    // get form
    var upload_form = document.getElementById("uploadForm")

    // create new form
    var form_data = new FormData(upload_form)
    form_data.append("csrfmiddlewaretoken", csrf);

    if (file_size > 5000) {
        $('#exampleModal2').modal('show');

    } else {
        // show modal
        $('#exampleModal').modal('show');

        await $.ajax({
            method: "POST",
            url: "/videos/",
            processData: false,
            contentType: false,
            data: form_data,
            success: function (res) {
                // clear form input
                $("#uploadForm").trigger("reset");

                // replace spinner with server response
                $("#video_score").replaceWith(`<p class='card-text fw-bold fs-1' id='video_score'>${res.mem_score}</p>`);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                // console error
                console.log(errorThrown)

                // show error text
                $("#video_score").replaceWith(`<p class='card-text fs-6' id='video_score'>An error has occured.</p>`);
            }
        })
    }


}