var elements = document.getElementsByTagName("*");
var filter edElements = Array.from(elements).filter(function(element) {
    // 排除 <a> 标签和带有 href 属性的元素
    return element.tagName !== "A" && !element.hasAttribute("href");
  });

var testCilck = function(){
  var randomElement = filteredElements[Math.floor(Math.random() * elements.length)];
  var event = new MouseEvent("click", {
      bubbles: true,
      cancelable: true,
      view: window
    });
    
  console.log(randomElement)

  if (randomElement.tagName === "A" || randomElement.hasAttribute("href")) {
    console.log("Skipped element:", randomElement);
    return;
  }

  

  randomElement.dispatchEvent(event)

} 

setInterval(testCilck, 1000)
