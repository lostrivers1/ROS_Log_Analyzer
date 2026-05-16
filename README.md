# ROS_Debug_Agent

ROS 导航系统日志自动化分析与 Debug 智能代理

## 项目概述
本项目构建了一个 **基于 AI/Agent 的 ROS 导航系统自动化日志分析与 Debug Agent**，用于实时收集、解析和诊断 ROS 导航栈日志，自动发现异常和性能瓶颈。该 Agent 能显著提升团队在 ROS 系统调试与优化过程中的效率。

---

## 核心功能
1. **自动化日志收集**：实时订阅 ROS 日志节点（如 `/rosout`、`/move_base`），结构化保存日志。  
2. **智能异常检测**：自动识别路径规划失败、局部避障异常、SLAM 漂移、传感器异常等，并提供根因分析。  
3. **多 Agent 协作分析**：多 Agent 并行处理日志，生成可视化报告及优化建议。  
4. **自动化回归验证**：在 Gazebo 仿真环境中复现问题，验证优化策略有效性。

---

## 技术优势
- 效率提升约 70%  
- 模块化设计，兼容 ROS 1/ROS 2  
- 高度自动化，无需人工干预  
- 数据驱动优化，支持历史日志训练模型

---

## 环境与依赖
- **操作系统**：Ubuntu 20.04 LTS（推荐）  
- **ROS 版本**：ROS Noetic（ROS 1）或 ROS 2 Foxy  
- **Python**：>=3.8  
- **依赖库**：
  ```bash
  pip install rospy rosgraph_msgs pandas numpy matplotlib
