var elements = document.getElementsByTagName("*");
var filteredElements = Array.from(elements).filter(function(element) {
    // 排除 <a> 标签和带有 href 属性的元素
    return element.tagName !== "A" && !element.hasAttribute("href");
  });

var test = function(){
    
var randomElement = filteredElements[Math.floor(Math.random() * elements.length)];
var event = new MouseEvent("click", {
    bubbles: true,
    cancelable: true,
    view: window
  });
console.log(randomElement.dispatchEvent(event))
console.log("event")

} 


for(let i=0;i<100;i++)
{
    setTimeout(() => {
    }, 1);

    test()
}