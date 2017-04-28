# -*- coding: utf-8 -*-
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
from ascendantAnalysis.grammar import Grammar
from ascendantAnalysis.ascendantAnalyzer import grammarPattern

grammar = Grammar(grammarPattern)