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
    '失去人性，失去很多；失去兽性，失去一切。',
    '我们都是阴沟里的虫子，但总还是得有人仰望星空。',
    '斩尽杀绝，这是对一个文明最高的重视。',
    '你们认为没有路，是因为没有学会不择手段.',
    '傻孩子们，快跑啊！',
    '小女孩，你看，我遵守了诺言。',
    '哦，要进画里了，孩子们，走好。',
]
function newQuote() {
    var randomNumber = Math.floor(Math.random() * quotes.length);
    document.getElementById('QuoteDisplay').innerHTML = quotes[randomNumber];
}