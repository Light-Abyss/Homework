var quotes = [
    '弱小和无知不是生存的障碍，傲慢才是。',
    '给岁月以文明，而不是给文明以岁月。',
    '虫子从来就没有被真正战胜过。',
    '没有永恒的敌人或同志，只有永恒的责任。',
    '前进！前进！！不择手段地前进！！！',
    '毁灭你，与你有何相干？',
    '这是计划的一部分。',
    '“自然选择”，前进四！',
    '不要回答！不要回答！！不要回答！！！',
    '碑是那么小，与其说是为了纪念，更像是为了忘却。',
    '一切都会逝去，只有死神永生。',
    '没关系的，都一样。',
    '不要返航，这里不是家！',
]
function newQuote() {
    var randomNumber = Math.floor(Math.random() * quotes.length);
    document.getElementById('QuoteDisplay').innerHTML = quotes[randomNumber];
}