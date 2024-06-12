# EIPGPT

The goal of this project is to create an AI powered tool to help complete repetitive tasks which are currently manually performed by the EIP staff related to new technology disclosure forms.

This API application serves as a basis that proves functionality of the ChatGPT API which can be further developed to create tools such as the following:


Pre Disclosure Form tool

An email is received by the EIP staff with a manuscript of a potential technology. The professor would like to know whether or not he should proceed with filling out a disclosure form for that technology and pursue ip protection or if their best interest is to publish the paper.

Functions
 Input
 - Upload document in form of a scientific paper manuscript
 Output
 - Identifies similar existing ip
  - Links to similar ip
   - ip.com, google patents
 - Market evaluation
  - Market size, growth, competitors



Disclosure Form Tool

A new tech disclosure form is received by the tech transfer office in the portal. This disclosure needs to be evaluated on whether the technology is worth it to pursue ip protection.

 Input
 - Disclosure form
 Output
  - Summary, procedures, advantages, disadvantages, potential applications, potential market/clients, competing technologies, questions/comments
 - Scoring system (different scores for categories)


 Potential GUIs:
 - Chrome extension to analyze disclosure forms directly on webpage without needing to download and upload disclosure form to a separate page.

 - Portal where you upload document and generates a report

 - GPT interface similar to the roadmap that guides you through the process of evaluating the disclosure form
  - ex: "can you identify the most likely markets for this product to succeed"
  -     "which market is best for the technology in terms of growth"
  -     "can you generate a list of industry connections that can be contacted"
