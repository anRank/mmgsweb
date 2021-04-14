from app import login_manager
from models.base import db
from flask_login import UserMixin
from datetime import datetime


# 用户表
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(100))
    name = db.Column(db.VARCHAR(100))
    password = db.Column(db.VARCHAR(100))
    tele = db.Column(db.String(20))
    is_manage = db.Column(db.Boolean)
    is_admin = db.Column(db.Boolean)
    using = db.Column(db.Boolean)


# 需要提供一个user_loader回调。此回调用于从会话中存储的用户ID重新加载用户对象。它应该unicode带有用户的ID，并返回相应的用户对象:
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))


# 古树基本属性表
class Basic_property(db.Model):
    __tablename__ = 'basic_property'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, primary_key=True, unique=True)  # 这里需要添加唯一性约束，才可以与外键关联
    zw_name = db.Column(db.VARCHAR(20))
    ld_name = db.Column(db.VARCHAR(20))
    bm_name = db.Column(db.VARCHAR(20))
    family = db.Column(db.VARCHAR(20))
    genus = db.Column(db.VARCHAR(20))
    town = db.Column(db.VARCHAR(20))
    village = db.Column(db.VARCHAR(20))
    place_name = db.Column(db.VARCHAR(20))
    palce = db.Column(db.VARCHAR(20))
    placing_character = db.Column(db.VARCHAR(20))
    owner = db.Column(db.VARCHAR(20))
    level = db.Column(db.VARCHAR(20))
    character_code = db.Column(db.Integer)
    jd_record = db.Column(db.VARCHAR(20))
    gh_unit = db.Column(db.VARCHAR(20))  # 管护单位
    username = db.Column(db.VARCHAR(20))  # 管护人
    is_signed = db.Column(db.BOOLEAN)
    using = db.Column(db.BOOLEAN)


# 古树动态属性表
class Dynamic_property(db.Model):
    __tablename__ = 'dynamic_property'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    describe = db.Column(db.VARCHAR(100))
    reason = db.Column(db.VARCHAR(100))
    affect_factor = db.Column(db.VARCHAR(100))
    height = db.Column(db.FLOAT)
    bust = db.Column(db.FLOAT)
    c_average = db.Column(db.FLOAT)
    c_dx = db.Column(db.FLOAT)
    c_nb = db.Column(db.FLOAT)
    g_vigor = db.Column(db.VARCHAR(100))
    g_environment = db.Column(db.VARCHAR(100))
    real_age = db.Column(db.Integer)
    estimate_age = db.Column(db.Integer)
    basis = db.Column(db.VARCHAR(100))
    history = db.Column(db.TEXT)
    history_pic = db.Column(db.VARCHAR(100))
    conserve_status = db.Column(db.VARCHAR(100))
    yhfz_status = db.Column(db.VARCHAR(100))
    investigate_id = db.Column(db.Integer)
    username = db.Column(db.VARCHAR(100))
    investigate_time = db.Column(db.TIMESTAMP)
    using = db.Column(db.Boolean)

    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('dynamic_p'))


# 古树地理属性表
class Geo_property(db.Model):
    __tablename__ = 'geo_property'
    dt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adcode = db.Column(db.Integer)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    elevation = db.Column(db.Float)
    aspect = db.Column(db.VARCHAR(100))
    slope = db.Column(db.Float)
    slope_position = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)

    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('geo_p'))


# 古树图片记录
class Pic_record(db.Model):
    __tablename__ = 'pic_record'
    pic_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.VARCHAR(100))
    explain = db.Column(db.VARCHAR(100))
    update_time = db.Column(db.TIMESTAMP)
    using = db.Column(db.Boolean)

    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('pic_ps'))


# 古树树牌信息确认
class Tree_brand(db.Model):
    __tablename__ = 'tree_brand'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    has_brand = db.Column(db.Boolean)
    is_right = db.Column(db.Boolean)
    content = db.Column(db.VARCHAR(100))
    brand_right = db.Column(db.VARCHAR(100))
    brand_pic = db.Column(db.VARCHAR(100))
    update_time = db.Column(db.TIMESTAMP)
    using = db.Column(db.Boolean)

    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('tree_bands'))


# # 生长势类型
class Growth_type(db.Model):
    __tablename__ = 'growth_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    growth = db.Column(db.VARCHAR(100))


# # 保护现状类型
class Protect_type(db.Model):
    __tablename__ = 'protect_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conserve_status = db.Column(db.VARCHAR(100))


# 养护复壮现状类型
class Yhfz_type(db.Model):
    __tablename__ = 'yhfz_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    yhfz_type = db.Column(db.VARCHAR(100))


# 树种科表
class Tree_species(db.Model):
    __tablename__ = 'tree_species'
    fid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.VARCHAR(100))


# 树种属表
class Tree_genus(db.Model):
    __tablename__ = 'tree_genus'
    gid = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.Integer, db.ForeignKey('tree_species.fid'))
    tree_s = db.relationship('Tree_species', backref=db.backref('tree_species'))
    genus = db.Column(db.VARCHAR(100))


# 树种分类表
class Tree_class(db.Model):
    __tablename__ = 'tree_class'
    cid = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer, db.ForeignKey('tree_genus.gid'))
    tree_g = db.relationship('Tree_genus', backref=db.backref('tree_classes'))
    zw_name = db.Column(db.VARCHAR(100))
    ld_name = db.Column(db.VARCHAR(100))


# 养护项目分类
class Yhxm_type(db.Model):
    __tablename__ = 'yhxm_type'
    y_id = db.Column(db.Integer, primary_key=True)
    yh_type = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 各类型养护项目对应的措施表
class Yh_measure(db.Model):
    __tablename__ = 'yh_measure'
    c_id = db.Column(db.Integer, primary_key=True)
    y_id = db.Column(db.Integer, db.ForeignKey('yhxm_type.y_id'))
    yh_type = db.relationship('Yhxm_type', backref=db.backref('yh_measures'))
    measure = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 各类型养护项目对应的处理方法表
class Yh_method(db.Model):
    __tablename__ = 'yh_method'
    f_id = db.Column(db.Integer, primary_key=True)
    y_id = db.Column(db.Integer, db.ForeignKey('yhxm_type.y_id'))
    yh_type = db.relationship('Yhxm_type', backref=db.backref('yh_methods'))
    method = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 养护记录
class Yh_record(db.Model):
    __tablename__ = 'yh_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer)
    yh_type = db.Column(db.VARCHAR(100))
    state = db.Column(db.VARCHAR(100))
    yh_id = db.Column(db.Integer)
    username = db.Column(db.VARCHAR(100))
    yh_time = db.Column(db.TIMESTAMP)
    using = db.Column(db.Boolean)


# 日常养护管理记录
class Daily_record(db.Model):
    __tablename__ = 'daily_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer)
    zw_name = db.Column(db.VARCHAR(100))
    yh_name = db.Column(db.VARCHAR(100))
    yh_time = db.Column(db.TIMESTAMP)
    lr_time = db.Column(db.TIMESTAMP)
    note = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 修剪记录
class Trim_record(db.Model):
    __tablename__ = 'trim_record'
    id = db.Column(db.Integer, primary_key=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    zw_name = db.Column(db.VARCHAR(100))
    yh_time = db.Column(db.TIMESTAMP)
    lr_time = db.Column(db.TIMESTAMP)
    reason = db.Column(db.VARCHAR(100))
    orientation = db.Column(db.VARCHAR(100))
    length = db.Column(db.Float)
    diameter = db.Column(db.Float)
    num = db.Column(db.Integer)
    method = db.Column(db.VARCHAR(100))
    note = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 树体保护记录
class Protect_record(db.Model):
    __tablename__ = 'protect_record'
    id = db.Column(db.Integer, primary_key=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('protect_records'))
    zw_name = db.Column(db.VARCHAR(100))
    yh_time = db.Column(db.TIMESTAMP)
    lr_time = db.Column(db.TIMESTAMP)
    property = db.Column(db.VARCHAR(100))
    measure = db.Column(db.VARCHAR(100))
    method = db.Column(db.VARCHAR(100))
    note = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 生长环境保护与改善记录
class GE_record(db.Model):
    __tablename__ = 'ge_record'
    id = db.Column(db.Integer, primary_key=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('ge_records'))
    zw_name = db.Column(db.VARCHAR(100))  # 树种
    yh_time = db.Column(db.TIMESTAMP)  # 养护时间
    lr_time = db.Column(db.TIMESTAMP)  # 录入时间
    property = db.Column(db.VARCHAR(100))  # 措施性质
    detail_name = db.Column(db.VARCHAR(100))  # 具体项目名称
    method = db.Column(db.VARCHAR(100))  # 处理方法
    note = db.Column(db.VARCHAR(100))  # 备注
    using = db.Column(db.Boolean)  # 是否有效


# 病虫害防治记录
class Pest(db.Model):
    __tablename__ = 'pest'
    id = db.Column(db.Integer, primary_key=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('pests'))
    zw_name = db.Column(db.VARCHAR(100))
    fz_type = db.Column(db.VARCHAR(100))
    method = db.Column(db.VARCHAR(100))
    concentration = db.Column(db.Float)
    bio_num = db.Column(db.Integer)
    trap_name = db.Column(db.VARCHAR(100))
    pest_name = db.Column(db.VARCHAR(100))
    efficiency = db.Column(db.VARCHAR(100))
    note = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 巡查工作记录
class Inspection_work(db.Model):
    __tablename__ = 'inspection_work'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('inspection_works'))
    zw_name = db.Column(db.VARCHAR(100))
    yh_time = db.Column(db.TIMESTAMP)
    lr_time = db.Column(db.TIMESTAMP)
    property = db.Column(db.VARCHAR(100))
    g_vigor = db.Column(db.VARCHAR(100))
    is_massage = db.Column(db.Boolean)
    direction = db.Column(db.VARCHAR(100))
    length = db.Column(db.Float)
    diameter = db.Column(db.Float)
    surroundings = db.Column(db.VARCHAR(100))
    grow_status = db.Column(db.VARCHAR(100))
    impact_describe = db.Column(db.VARCHAR(100))
    phenological_describe = db.Column(db.VARCHAR(100))
    note = db.Column(db.VARCHAR(100))
    using = db.Column(db.Boolean)


# 天气
class Weather(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lr_time = db.Column(db.TIMESTAMP)
    temp = db.Column(db.Integer)
    rh = db.Column(db.Integer)
    wind_class = db.Column(db.VARCHAR(100))
    wind_dir = db.Column(db.VARCHAR(100))
    text = db.Column(db.VARCHAR(100))


# 体检项目记录
class Tjxm_recod(db.Model):
    __tablename__ = 'tjxm_record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('tjxm_records'))
    type = db.Column(db.VARCHAR(100))
    t_id = db.Column(db.Integer)
    username = db.Column(db.VARCHAR(100))
    status = db.Column(db.VARCHAR(100))
    time = db.Column(db.TIMESTAMP)
    using = db.Column(db.Boolean)


# 生长环境评估分析
class GE_analysis(db.Model):
    __tablename__ = 'ge_analysis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('ge_analysis'))
    elevation = db.Column(db.Float)
    habitat_type = db.Column(db.VARCHAR(100))
    plain_type = db.Column(db.VARCHAR(100))
    highland_type = db.Column(db.VARCHAR(100))
    aspect = db.Column(db.VARCHAR(100))
    slope = db.Column(db.Float)
    slope_position = db.Column(db.VARCHAR(100))
    is_pollution = db.Column(db.Boolean)
    varia = db.Column(db.VARCHAR(100))
    soil_texture = db.Column(db.VARCHAR(100))
    soil_capacity = db.Column(db.Float)
    organic_content = db.Column(db.VARCHAR(100))
    sample_result = db.Column(db.VARCHAR(100))
    hydrolyze_N = db.Column(db.Float)
    valid_P = db.Column(db.Float)
    rapid_K = db.Column(db.Float)
    saltness = db.Column(db.Float)
    ec_value = db.Column(db.Float)
    ph_value = db.Column(db.Float)
    is_buried = db.Column(db.Boolean)
    buried_depth = db.Column(db.Float)
    root_water = db.Column(db.Float)
    protect_E = db.Column(db.Float)
    protect_W = db.Column(db.Float)
    protect_S = db.Column(db.Float)
    protect_N = db.Column(db.Float)
    protect_pic = db.Column(db.VARCHAR(100))
    other_plants = db.Column(db.VARCHAR(100))
    evaluation = db.Column(db.VARCHAR(100))
    envoriment_problem = db.Column(db.VARCHAR(100))
    has_structures = db.Column(db.Boolean)
    structures_type = db.Column(db.VARCHAR(100))
    structures_affect = db.Column(db.VARCHAR(100))
    nutrient_status = db.Column(db.VARCHAR(100))
    pic_path = db.Column(db.VARCHAR(100))
    update_time = db.Column(db.TIMESTAMP)
    using = db.Column(db.Boolean)


# 生长势分析
class GP_analysis(db.Model):
    __tablename__ = "gp_analysis"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('gp_analysis'))
    shoot_type = db.Column(db.VARCHAR(100))
    normal_blade_rate = db.Column(db.VARCHAR(100))
    blade_persistent = db.Column(db.VARCHAR(100))
    growth_vigor = db.Column(db.VARCHAR(100))
    chlorophyll = db.Column(db.Float)
    Fo = db.Column(db.Float)
    Fm = db.Column(db.Float)
    photosynthetic = db.Column(db.Float)
    pic_path = db.Column(db.VARCHAR(100))
    update_time = db.Column(db.TIMESTAMP)


# 已采取复壮保护措施情况与分析
class Fzbh_analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))
    basic_p = db.relationship('Basic_property', backref=db.backref('fzbh_analysis'))
    protect = db.Column(db.VARCHAR(100))  # *地上保护措施
    soil_improve = db.Column(db.VARCHAR(100))  # *地下土壤改良措施
    is_block = db.Column(db.Boolean)  # *是否封堵树洞
    fit_status = db.Column(db.VARCHAR(100))  # *（封堵）与树体贴合情况
    drain_hole = db.Column(db.VARCHAR(100))  # *（封堵）排水孔和排湿孔
    tech_level = db.Column(db.VARCHAR(100))  # *（封堵）工艺水平
    outer = db.Column(db.VARCHAR(100))  # *（封堵）外层处理
    clean_status = db.Column(db.VARCHAR(100))  # *（未封堵）内壁清理程度
    antiseptic = db.Column(db.VARCHAR(100))  # *（未封堵）内壁防腐处理
    is_support = db.Column(db.Boolean)  # *是否存在支撑
    hard_support = db.Column(db.Boolean)  # *（有支撑）硬支撑几处
    protaging = db.Column(db.Boolean)  # *（有支撑）拉纤几处
    steady = db.Column(db.VARCHAR(100))  # （有支撑）稳固情况
    support_type = db.Column(db.VARCHAR(100))  # *（有支撑）支撑类型
    support_isrea = db.Column(db.VARCHAR(100))  # （有支撑）支撑部位是否合理
    hoop_status = db.Column(db.VARCHAR(100))  # *（有支撑）抱箍情况
    rubber_is = db.Column(db.Boolean)  # （有支撑）橡胶垫设置是否合理
    hoop_is = db.Column(db.Boolean)  # （有支撑）抱箍设置是否合理
    has_ditch = db.Column(db.Boolean)  # *是否有复壮沟
    ditch_type = db.Column(db.VARCHAR(100))  # *（有）复壮沟类型
    ditch_num = db.Column(db.Integer)  # *（有）复壮沟数量
    ditch_width = db.Column(db.Float)  # 复壮沟宽度
    ditch_length = db.Column(db.Float)  # 复壮沟总长度
    pipe_num = db.Column(db.Integer)  # *（有）通气管数量
    matrix_constitute = db.Column(db.VARCHAR(100))  # 复壮沟基质组成
    position_is = db.Column(db.VARCHAR(100))  # 复壮沟位置设置是否合理
    well_num = db.Column(db.Integer)  # *（有）渗井数量
    capillary_roots = db.Column(db.VARCHAR(100))  # 复壮沟毛细根生长情况
    protect_eval = db.Column(db.VARCHAR(100))  # 现有复壮保护措施评价
    pic = db.Column(db.VARCHAR(100))  # 特征照片
    update_time = db.Column(db.TIMESTAMP)  # 更新时间
    using = db.Column(db.Boolean)  # 是否有效


# 树体损伤情况评估
class Stss_analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))  # 古树编号
    basic_p = db.relationship('Basic_property', backref=db.backref('stss_analysis'))  #
    base1 = db.Column(db.VARCHAR(100))  # 树干基部-树皮损伤比例
    pic_base1 = db.Column(db.VARCHAR(100))  # (照片)树干基部-树皮损伤比例
    base2 = db.Column(db.VARCHAR(100))  # 树干基部-木质部损伤（未达心材）比例
    pic_base2 = db.Column(db.VARCHAR(100))  # (照片)树干基部-木质部损伤（未达心材）比例
    base3 = db.Column(db.VARCHAR(100))  # 树干基部-木质部损伤（达到心材）比例
    pic_base3 = db.Column(db.VARCHAR(100))  # (照片)树干基部-木质部损伤（达到心材）比例
    trunk1 = db.Column(db.VARCHAR(100))  # 树干-树皮损伤比例
    pic_trunk1 = db.Column(db.VARCHAR(100))  # (照片)树干-树皮损伤比例
    trunk2 = db.Column(db.VARCHAR(100))  # 树干-木质部（未达心材）比例
    pic_trunk2 = db.Column(db.VARCHAR(100))  # (照片)树干-木质部（未达心材）比例
    trunk3 = db.Column(db.VARCHAR(100))  # 树干-木质部（达到心材）损伤比例
    pic_trunk3 = db.Column(db.VARCHAR(100))  # (照片)树干-木质部（达到心材）损伤比例
    skeleton1 = db.Column(db.VARCHAR(100))  # 构成骨架大枝-树皮损伤比例
    pic_ske1 = db.Column(db.VARCHAR(100))  # (照片)构成骨架大枝-树皮损伤比例
    skeleton2 = db.Column(db.VARCHAR(100))  # 构成骨架大枝-木质部（未达心材）比例
    pic_ske2 = db.Column(db.VARCHAR(100))  # (照片)构成骨架大枝-木质部（未达心材）比例
    skeleton3 = db.Column(db.VARCHAR(100))  # 构成骨架大枝-木质部（达到心材）比例
    pic_ske3 = db.Column(db.VARCHAR(100))  # (照片)构成骨架大枝-木质部（达到心材）比例
    damage_status = db.Column(db.VARCHAR(100))  # 损伤情况评价
    update_time = db.Column(db.TIMESTAMP)  # 更新时间
    using = db.Column(db.Boolean)  # 是否有效


# 树体倾斜、空腐情况检测
class Qxkf_detect(db.Model):
    __tablename__ = "qxkf_detect"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))  # 古树编号
    basic_p = db.relationship('Basic_property', backref=db.backref('qxkf_detects'))  #
    base_loose = db.Column(db.VARCHAR(100))  # *树基松动结果
    pic_1 = db.Column(db.VARCHAR(100))  # *树基松动照片
    root_rot = db.Column(db.VARCHAR(100))  # *根部腐朽结果
    pic_2 = db.Column(db.VARCHAR(100))  # *根部腐朽照片
    root_bare = db.Column(db.VARCHAR(100))  # *根部裸露结果
    bare_length = db.Column(db.Float)  # *根部裸露总长度
    pic_3 = db.Column(db.VARCHAR(100))  # *根部裸露照片
    has_absound = db.Column(db.Boolean)  # *主干异常音
    trunk_inclined = db.Column(db.VARCHAR(100))  # 主干倾斜结果
    pic_4 = db.Column(db.VARCHAR(100))  # 主干倾斜照片
    has_abbranch = db.Column(db.VARCHAR(100))  # 分枝点部位异常结果
    pic_5 = db.Column(db.VARCHAR(100))  # 分枝点部位异常照片
    lopsided = db.Column(db.VARCHAR(100))  # 偏冠结果
    pic_6 = db.Column(db.VARCHAR(100))  # 偏冠照片
    deadwood = db.Column(db.VARCHAR(100))  # 枯枝结果
    pic_7 = db.Column(db.VARCHAR(100))  # 枯枝照片
    twig = db.Column(db.VARCHAR(100))  # 枝条整理留茬结果
    pic_8 = db.Column(db.VARCHAR(100))  # 枝条整理留茬照片
    empty_rot_rate = db.Column(db.Float)  # 主干空腐率
    qxkf_eval = db.Column(db.VARCHAR(100))  # 倾斜空腐情况评价
    update_time = db.Column(db.TIMESTAMP)  # 更新时间
    using = db.Column(db.Boolean)  # 是否有效


# 病虫害发生情况分析
class Bch_analysis(db.Model):
    __tablename__ = 'bch_analysis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tree_code = db.Column(db.Integer, db.ForeignKey('basic_property.tree_code'))  # 古树编号
    basic_p = db.relationship('Basic_property', backref=db.backref('bch_analysis'))
    bmoth_status = db.Column(db.VARCHAR(100))  # 树干基部-蛀干害虫情况
    bmoth_name = db.Column(db.VARCHAR(100))  # 树干基部-害虫名称
    bdisease_status = db.Column(db.VARCHAR(100))  # 树干基部-病害情况
    bdisease_name = db.Column(db.VARCHAR(100))  # 树干基部-病害名称
    base_pic = db.Column(db.VARCHAR(100))  # 树干基部-特征照片
    tmoth_status = db.Column(db.VARCHAR(100))  # 树干-蛀干害虫情况
    tmoth_name = db.Column(db.VARCHAR(100))  # 树干-蛀干害虫名称
    tdisease_status = db.Column(db.VARCHAR(100))  # 树干-病害情况
    tdisease_name = db.Column(db.VARCHAR(100))  # 树干-病害名称
    trunk_pic = db.Column(db.VARCHAR(100))  # 树干-特征照片
    smoth_status = db.Column(db.VARCHAR(100))  # 构成骨架大枝-蛀干害虫情况
    smoth_name = db.Column(db.VARCHAR(100))  # 构成骨架大枝-蛀干害虫名称
    sdisease_status = db.Column(db.VARCHAR(100))  # 构成骨架大枝-病害情况
    sdisease_name = db.Column(db.VARCHAR(100))  # 构成骨架大枝-病害名称
    ske_pic = db.Column(db.VARCHAR(100))  # 构成骨架大枝-特征照片
    blade_status = db.Column(db.VARCHAR(100))  # 叶片-病害情况
    blade_name = db.Column(db.VARCHAR(100))  # 叶片-病害名称
    blade_pic = db.Column(db.VARCHAR(100))  # 叶片-特征照片
    branch_status = db.Column(db.VARCHAR(100))  # 枝梢-蛀干害虫情况
    branch_name = db.Column(db.VARCHAR(100))  # 枝梢-蛀干害虫名称
    branch_pic = db.Column(db.VARCHAR(100))  # 枝梢-特征照片
    total_eval = db.Column(db.VARCHAR(100))  # 总体评价
    update_time = db.Column(db.TIMESTAMP)  # 更新时间
    using = db.Column(db.Boolean)  # 是否有效
