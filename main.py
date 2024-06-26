structure = {
    "第1章 互联网的增长引擎——推荐系统": [
        {
            "1.1 为什么推荐系统是互联网的增长引擎": [
                "1.1.1 推荐系统的作用和意义",
                "1.1.2 推荐系统与YouTube的观看时长增长",
                "1.1.3 推荐系统与电商网站的收入增长"
            ]
        },
        {
            "1.2 推荐系统的架构": [
                "1.2.1 推荐系统的逻辑框架",
                "1.2.2 推荐系统的技术架构",
                "1.2.3 推荐系统的数据部分",
                "1.2.4 推荐系统的模型部分",
                "1.2.5 深度学习对推荐系统的革命性贡献",
                "1.2.6 把握整体，补充细节"
            ]
        },
        "1.3 本书的整体结构"
    ],
    "第2章 前深度学习时代——推荐系统的进化之路": [
        "2.1 传统推荐模型的演化关系图",
        {
            "2.2 协同过滤——经典的推荐算法": [
                "2.2.1 什么是协同过滤",
                "2.2.2 用户相似度计算",
                "2.2.3 终结果的排序",
                "2.2.4 ItemCF",
                "2.2.5 UserCF与ItemCF的应用场景",
                "2.2.6 协同过滤的下一步发展"
            ]
        },
        {
            "2.3 矩阵分解算法——协同过滤的进化": [
                "2.3.1 矩阵分解算法的原理",
                "2.3.2 矩阵分解的求解过程",
                "2.3.3 消除用户和物品打分的偏差",
                "2.3.4 矩阵分解的优点和局限性"
            ]
        },
        {
            "2.4 逻辑回归——融合多种特征的推荐模型": [
                "2.4.1 基于逻辑回归模型的推荐流程",
                "2.4.2 逻辑回归模型的数学形式",
                "2.4.3 逻辑回归模型的训练方法",
                "2.4.4 逻辑回归模型的优势",
                "2.4.5 逻辑回归模型的局限性"
            ]
        },
        {
            "2.5 从FM到FFM——自动特征交叉的解决方案": [
                "2.5.1 POLY2模型——特征交叉的开始",
                "2.5.2 FM模型——隐向量特征交叉",
                "2.5.3 FFM模型——引入特征域的概念",
                "2.5.4 从POLY2到FFM的模型演化过程"
            ]
        },
        {
            "2.6 GBDT+LR——特征工程模型化的开端": [
                "2.6.1 GBDT+LR组合模型的结构",
                "2.6.2 GBDT进行特征转换的过程",
                "2.6.3 GBDT+LR 组合模型开启的特征工程新趋势"
            ]
        },
        {
            "2.7 LS-PLM——阿里巴巴曾经的主流推荐模型": [
                "2.7.1 LS-PLM 模型的主要结构",
                "2.7.2 LS-PLM模型的优点",
                "2.7.3 从深度学习的角度重新审视LS-PLM模型"
            ]
        },
        "2.8 总结——深度学习推荐系统的前夜"
    ],
    "第3章 浪潮之巅——深度学习在推荐系统中的应用": [
        "3.1 深度学习推荐模型的演化关系图",
        {
            "3.2 AutoRec——单隐层神经网络推荐模型": [
                "3.2.1 AutoRec模型的基本原理",
                "3.2.2 AutoRec模型的结构",
                "3.2.3 基于AutoRec模型的推荐过程",
                "3.2.4 AutoRec模型的特点和局限性"
            ]
        },
        {
            "3.3 Deep Crossing模型——经典的深度学习架构": [
                "3.3.1 Deep Crossing模型的应用场景",
                "3.3.2 Deep Crossing模型的网络结构",
                "3.3.3 Deep Crossing模型对特征交叉方法的革命"
            ]
        },
        {
            "3.4 NeuralCF模型——CF与深度学习的结合": [
                "3.4.1 从深度学习的视角重新审视矩阵分解模型",
                "3.4.2 NeuralCF模型的结构",
                "3.4.3 NeuralCF模型的优势和局限性"
            ]
        },
        {
            "3.5 PNN模型——加强特征交叉能力": [
                "3.5.1 PNN模型的网络架构",
                "3.5.2 Product层的多种特征交叉方式",
                "3.5.3 PNN模型的优势和局限性"
            ]
        },
        {
            "3.6 Wide&Deep 模型——记忆能力和泛化能力的综合": [
                "3.6.1 模型的记忆能力与泛化能力",
                "3.6.2 Wide&Deep模型的结构",
                "3.6.3 Wide&Deep模型的进化——Deep&Cross模型",
                "3.6.4 Wide&Deep模型的影响力"
            ]
        },
        {
            "3.7 FM与深度学习模型的结合": [
                "3.7.1 FNN——用FM的隐向量完成Embedding层初始化",
                "3.7.2 DeepFM——用FM代替Wide部分",
                "3.7.3 NFM——FM的神经网络化尝试",
                "3.7.4 基于FM的深度学习模型的优点和局限性"
            ]
        },
        {
            "3.8 注意力机制在推荐模型中的应用": [
                "3.8.1 AFM——引入注意力机制的FM",
                "3.8.2 DIN——引入注意力机制的深度学习网络",
                "3.8.3 注意力机制对推荐系统的启发"
            ]
        },
        {
            "3.9 DIEN——序列模型与推荐系统的结合": [
                "3.9.1 DIEN的“进化”动机",
                "3.9.2 DIEN模型的架构",
                "3.9.3 兴趣抽取层的结构",
                "3.9.4 兴趣进化层的结构",
                "3.9.5 序列模型对推荐系统的启发"
            ]
        },
        {
            "3.10 强化学习与推荐系统的结合": [
                "3.10.1 深度强化学习推荐系统框架",
                "3.10.2 深度强化学习推荐模型",
                "3.10.3 DRN的学习过程",
                "3.10.4 DRN的在线学习方法——竞争梯度下降算法",
                "3.10.5 强化学习对推荐系统的启发"
            ]
        },
        "3.11 总结——推荐系统的深度学习时代"
    ],
    "第4章 Embedding技术在推荐系统中的应用": [
        {
            "4.1 什么是Embedding": [
                "4.1.1 词向量的例子",
                "4.1.2 Embedding 技术在其他领域的扩展",
                "4.1.3 Embedding 技术对于深度学习推荐系统的重要性"
            ]
        },
        {
            "4.2 Word2vec——经典的Embedding方法": [
                "4.2.1 什么是Word2vec",
                "4.2.2 Word2vec模型的训练过程",
                "4.2.3 Word2vec的“负采样”训练方法",
                "4.2.4 Word2vec对Embedding技术的奠基性意义"
            ]
        },
        {
            "4.3 Item2vec——Word2vec 在推荐系统领域的推广": [
                "4.3.1 Item2vec的基本原理",
                "4.3.2 “广义”的Item2vec",
                "4.3.3 Item2vec方法的特点和局限性"
            ]
        },
        {
            "4.4 Graph Embedding——引入更多结构信息的图嵌入技术": [
                "4.4.1 DeepWalk——基础的Graph Embedding方法",
                "4.4.2 Node2vec——同质性和结构性的权衡",
                "4.4.3 EGES——阿里巴巴的综合性Graph Embedding方法"
            ]
       
        },
        {
            "4.5 Embedding与深度学习推荐系统的结合": [
                "4.5.1 深度学习网络中的Embedding层",
                "4.5.2 Embedding的预训练方法",
                "4.5.3 Embedding作为推荐系统召回层的方法"
            ]
        },
        {
            "4.6 局部敏感哈希——让Embedding插上翅膀的快速搜索方法": [
                "4.6.1 “快速”Embedding近邻搜索",
                "4.6.2 局部敏感哈希的基本原理",
                "4.6.3 局部敏感哈希多桶策略"
            ]
        },
        "4.7 总结——深度学习推荐系统的核心操作"
    ],
    "第5章 多角度审视推荐系统": [
        {
            "5.1 推荐系统的特征工程": [
                "5.1.1 构建推荐系统特征工程的原则",
                "5.1.2 推荐系统中的常用特征",
                "5.1.3 常用的特征处理方法",
                "5.1.4 特征工程与业务理解"
            ]
        },
        {
            "5.2 推荐系统召回层的主要策略": [
                "5.2.1 召回层和排序层的功能特点",
                "5.2.2 多路召回策略",
                "5.2.3 基于Embedding的召回方法"
            ]
        },
        {
            "5.3 推荐系统的实时性": [
                "5.3.1 为什么说推荐系统的实时性是重要的",
                "5.3.2 推荐系统“特征”的实时性",
                "5.3.3 推荐系统“模型”的实时性",
                "5.3.4 用“木桶理论”看待推荐系统的迭代升级"
            ]
        },
        {
            "5.4 如何合理设定推荐系统中的优化目标": [
                "5.4.1 YouTube以观看时长为优化目标的合理性",
                "5.4.2 模型优化和应用场景的统一性",
                "5.4.3 优化目标是和其他团队的接口性工作"
            ]
        },
        {
            "5.5 推荐系统中比模型结构更重要的是什么": [
                "5.5.1 有解决推荐问题的“银弹”吗",
                "5.5.2 Netflix对用户行为的观察",
                "5.5.3 观察用户行为，在模型中加入有价值的用户信息",
                "5.5.4 DIN模型的改进动机",
                "5.5.5 算法工程师不能只是一个“炼金术士”"
            ]
        },
        {
            "5.6 冷启动的解决办法": [
                "5.6.1 基于规则的冷启动过程",
                "5.6.2 丰富冷启动过程中可获得的用户和物品特征",
                "5.6.3 利用主动学习、迁移学习和“探索与利用”机制",
                "5.6.4 “巧妇难为无米之炊”的困境"
            ]
        },
        {
            "5.7 探索与利用": [
                "5.7.1 传统的探索与利用方法",
                "5.7.2 个性化的探索与利用方法",
                "5.7.3 基于模型的探索与利用方法",
                "5.7.4 “探索与利用”机制在推荐系统中的应用"
            ]
        }
    ],
    "第6章 深度学习推荐系统的工程实现": [
        {
            "6.1 推荐系统的数据流": [
                "6.1.1 批处理大数据架构",
                "6.1.2 流计算大数据架构",
                "6.1.3 Lambda架构",
                "6.1.4 Kappa架构",
                "6.1.5 大数据平台与推荐系统的整合"
            ]
        },
        {
            "6.2 推荐模型离线训练之Spark MLlib": [
                "6.2.1 Spark的分布式计算原理",
                "6.2.2 Spark MLlib的模型并行训练原理",
                "6.2.3 Spark MLlib并行训练的局限性"
            ]
        },
        {
            "6.3 推荐模型离线训练之Parameter Server": [
                "6.3.1 Parameter Server的分布式训练原理",
                "6.3.2 一致性与并行效率之间的取舍",
                "6.3.3 多server节点的协同和效率问题",
                "6.3.4 Parameter Server技术要点总结"
            ]
        },
        {
            "6.4 推荐模型离线训练之TensorFlow": [
                "6.4.1 TensorFlow的基本原理",
                "6.4.2 TensorFlow基于任务关系图的并行训练过程",
                "6.4.3 TensorFlow的单机训练与分布式训练模式",
                "6.4.4 TensorFlow技术要点总结"
            ]
        },
        {
            "6.5 深度学习推荐模型的上线部署": [
                "6.5.1 预存推荐结果或Embedding结果",
                "6.5.2 自研模型线上服务平台",
                "6.5.3 预训练Embedding+轻量级线上模型",
                "6.5.4 利用PMML转换并部署模型",
                "6.5.5 TensorFlow Serving",
                "6.5.6 灵活选择模型服务方法"
            ]
        },
        {
            "6.6 工程与理论之间的权衡": [
                "6.6.1 工程师职责的本质",
                "6.6.2 Redis容量和模型上线方式之间的权衡",
                "6.6.3 研发周期限制和技术选型的权衡",
                "6.6.4 硬件平台环境和模型结构间的权衡",
                "6.6.5 处理好整体和局部的关系"
            ]
        }
    ],
    "第7章 推荐系统的评估": [
        {
            "7.1 离线评估方法与基本评价指标": [
                "7.1.1 离线评估的主要方法",
                "7.1.2 离线评估的指标"
            ]
        },
        {
            "7.2 直接评估推荐序列的离线指标": [
                "7.2.1 P-R曲线",
                "7.2.2 ROC曲线",
                "7.2.3 平均精度均值",
                "7.2.4 合理选择评估指标"
            ]
        },
        {
            "7.3 更接近线上环境的离线评估方法——Replay": [
                "7.3.1 模型评估的逻辑闭环",
                "7.3.2 动态离线评估方法",
                "7.3.3 Netflix的Replay评估方法实践"
            ]
        },
        {
            "7.4 A/B测试与线上评估指标": [
                "7.4.1 什么是A/B测试",
                "7.4.2 A/B测试的“分桶”原则",
                "7.4.3 线上A/B测试的评估指标"
            ]
        },
        {
            "7.5 快速线上评估方法——Interleaving": [
                "7.5.1 传统A/B测试存在的统计学问题",
                "7.5.2 Interleaving方法的实现",
                "7.5.3 Interleaving方法与传统A/B测试的灵敏度比较",
                "7.5.4 Interleaving方法指标与A/B测试指标的相关性",
                "7.5.5 Interleaving方法的优点与缺点"
            ]
        },
        "7.6 推荐系统的评估体系"
    ],
    "第8章 深度学习推荐系统的前沿实践": [
        {
            "8.1 Facebook的深度学习推荐系统": [
                "8.1.1 推荐系统应用场景",
                "8.1.2 以GBDT+LR组合模型为基础的CTR预估模型",
                "8.1.3 实时数据流架构",
                "8.1.4 降采样和模型校正",
                "8.1.5 Facebook GBDT+LR组合模型的工程实践",
                "8.1.6 Facebook的深度学习模型DLRM",
                "8.1.7 DLRM模型并行训练方法",
                "8.1.8 DLRM模型的效果",
                "8.1.9 Facebook深度学习推荐系统总结"
            ]
        },
        {
            "8.2 Airbnb基于Embedding的实时搜索推荐系统": [
                "8.2.1 推荐系统应用场景",
                "8.2.2 基于短期兴趣的房源Embedding方法",
                "8.2.3 基于长期兴趣的用户Embedding和房源Embedding",
               
                "8.2.4 Airbnb搜索词的Embedding",
                "8.2.5 Airbnb的实时搜索排序模型及其特征工程",
                "8.2.6 Airbnb实时搜索推荐系统总结"
            ]
        },
        {
            "8.3 YouTube深度学习视频推荐系统": [
                "8.3.1 推荐系统应用场景",
                "8.3.2 YouTube推荐系统架构",
                "8.3.3 候选集生成模型",
                "8.3.4 候选集生成模型独特的线上服务方法",
                "8.3.5 排序模型",
                "8.3.6 训练和测试样本的处理",
                "8.3.7 如何处理用户对新视频的偏好",
                "8.3.8 YouTube深度学习视频推荐系统总结"
            ]
        },
        {
            "8.4 阿里巴巴深度学习推荐系统的进化": [
                "8.4.1 推荐系统应用场景",
                "8.4.2 阿里巴巴的推荐模型体系",
                "8.4.3 阿里巴巴深度学习推荐模型的进化过程",
                "8.4.4 模型服务模块的技术架构",
                "8.4.5 阿里巴巴推荐技术架构总结"
            ]
        }
    ]
}


import os
import json
from typing import Union, Dict, List, Any

def create_directories_and_files(
    base_path: str, 
    structure: Dict[str, Any], 
    readme_file, 
    parent_path: str = "", 
    level: int = 1
):
    """
    根据给定的目录结构创建目录和文件，并生成 README.md 文件。

    Args:
        base_path (str): 根目录路径。
        structure (Dict[str, Any]): 目录结构的嵌套字典。
        readme_file (File): 用于写入README内容的文件对象。
        parent_path (str): 父目录路径。
        level (int): 目录的层级，用于确定 README 标题级别。

    Returns:
        None
    """
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("/", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
        else:
            # 创建文件并写入初始内容
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# 推荐系统\n\n")
        readme_file.write("这是一个关于推荐系统的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()