  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;

    // call a function whenever the cursor moves:
    if (document.getElementById("clickbox")){
    document.onmousemove = elementDrag;
    document.onmouseup = closeDragElement;
    }



  }
