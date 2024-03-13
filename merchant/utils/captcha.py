from PIL import Image, ImageDraw, ImageFont
import random
import io
import  os
def generate_captcha(width=120, height=50, length=4, font_size=50):
    """
    生成验证码图片和验证码字符串

    参数：
    width: 图片宽度，默认为200像素
    height: 图片高度，默认为100像素
    length: 验证码长度，默认为4个字符
    font_size: 字体大小，默认为50像素

    返回值：
    captcha_text: 生成的验证码字符串
    img_io: 图片的字节流
    """

    # 生成随机验证码字符串
    captcha_text = ''.join(random.choices('0123456789', k=length))

    # 创建白色背景图片
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # 获取项目根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 指定字体文件的路径
    FONT_PATH = os.path.join(BASE_DIR, 'static', 'font', 'arial.ttf')
    # 加载字体
    font = ImageFont.truetype(FONT_PATH, font_size)

    # 计算文本绘制位置
    text_width, text_height = draw.textbbox((0, 0), captcha_text, font=font)[2:]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # 绘制文本
    draw.text((x, y), captcha_text, fill='black', font=font)

    # 添加干扰线
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill='black', width=2)

    # 添加干扰点
    for _ in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill='black')

    # 将图片保存到内存中
    img_io = io.BytesIO()
    image.save(img_io, format='PNG')
    img_io.seek(0)

    return captcha_text, img_io
