StatusInfoDict = {"Poisoned": (2, -1),  # (Damage,Duration)
                  "Badly Poisoned": (6, -1),
                  "Burned": (6, -1),
                  "Frozen": (0, 5),
                  "Paralyzed": (0, 3)
                  }
###########################################
StageDict = {0: 0.5,  # Levels for ATK,DEF,SPATK,SPDEF
             1: 0.52,
             2: 0.54,
             3: 0.56,
             4: 0.58,
             5: 0.6,
             6: 0.63,
             7: 0.67,
             8: 0.7,
             9: 0.8,
             10: 1,
             11: 1.2,
             12: 1.3,
             13: 1.4,
             14: 1.5,
             15: 1.6,
             16: 1.65,
             17: 1.7,
             18: 1.75,
             19: 1.8,
             20: 1.85
             }
###########################################
A = 0
B = 0.7
C = 1
D = 1.4

DamageDict = {"Normal": {"Normal": C,  # DamageDict[Attacker][Target]
                         "Fire": C,
                         "Water": C,
                         "Electric": C,
                         "Grass": C,
                         "Ice": C,
                         "Fighting": C,
                         "Poison": C,
                         "Ground": C,
                         "Flying": C,
                         "Psychic": C,
                         "Bug": C,
                         "Rock": B,
                         "Ghost": A,
                         "Dragon": C,
                         "Dark": C,
                         "Steel": B,
                         "Fairy": C,
                         "Typeless": C
                         },
              "Fire": {"Normal": C,
                       "Fire": B,
                       "Water": B,
                       "Electric": C,
                       "Grass": D,
                       "Ice": D,
                       "Fighting": C,
                       "Poison": C,
                       "Ground": C,
                       "Flying": C,
                       "Psychic": C,
                       "Bug": D,
                       "Rock": B,
                       "Ghost": C,
                       "Dragon": B,
                       "Dark": C,
                       "Steel": D,
                       "Fairy": C,
                       "Typeless": C
                       },
              "Water": {"Normal": C,
                        "Fire": D,
                        "Water": B,
                        "Electric": C,
                        "Grass": B,
                        "Ice": C,
                        "Fighting": C,
                        "Poison": C,
                        "Ground": D,
                        "Flying": C,
                        "Psychic": C,
                        "Bug": C,
                        "Rock": D,
                        "Ghost": C,
                        "Dragon": B,
                        "Dark": C,
                        "Steel": C,
                        "Fairy": C,
                        "Typeless": C,
                        },
              "Grass": {"Normal": C,
                        "Fire": B,
                        "Water": D,
                        "Electric": C,
                        "Grass": B,
                        "Ice": C,
                        "Fighting": C,
                        "Poison": B,
                        "Ground": D,
                        "Flying": B,
                        "Psychic": C,
                        "Bug": B,
                        "Rock": D,
                        "Ghost": C,
                        "Dragon": B,
                        "Dark": C,
                        "Steel": B,
                        "Fairy": C,
                        "Typeless": C,
                        },
              "Electric": {"Normal": C,
                           "Fire": C,
                           "Water": D,
                           "Electric": B,
                           "Grass": B,
                           "Ice": C,
                           "Fighting": C,
                           "Poison": C,
                           "Ground": A,
                           "Flying": D,
                           "Psychic": C,
                           "Bug": C,
                           "Rock": C,
                           "Ghost": C,
                           "Dragon": B,
                           "Dark": C,
                           "Steel": C,
                           "Fairy": C,
                           "Typeless": C,
                           },
              "Ice": {"Normal": C,
                      "Fire": B,
                      "Water": B,
                      "Electric": C,
                      "Grass": D,
                      "Ice": B,
                      "Fighting": C,
                      "Poison": C,
                      "Ground": D,
                      "Flying": D,
                      "Psychic": C,
                      "Bug": C,
                      "Rock": C,
                      "Ghost": C,
                      "Dragon": D,
                      "Dark": C,
                      "Steel": B,
                      "Fairy": C,
                      "Typeless": C,
                      },
              "Fighting": {"Normal": D,
                           "Fire": C,
                           "Water": C,
                           "Electric": C,
                           "Grass": C,
                           "Ice": D,
                           "Fighting": C,
                           "Poison": B,
                           "Ground": C,
                           "Flying": B,
                           "Psychic": B,
                           "Bug": B,
                           "Rock": D,
                           "Ghost": A,
                           "Dragon": C,
                           "Dark": D,
                           "Steel": D,
                           "Fairy": B,
                           "Typeless": C,
                           },
              "Poison": {"Normal": C,
                         "Fire": C,
                         "Water": C,
                         "Electric": C,
                         "Grass": D,
                         "Ice": C,
                         "Fighting": C,
                         "Poison": B,
                         "Ground": B,
                         "Flying": C,
                         "Psychic": C,
                         "Bug": C,
                         "Rock": B,
                         "Ghost": B,
                         "Dragon": C,
                         "Dark": C,
                         "Steel": A,
                         "Fairy": D,
                         "Typeless": C,
                         },
              "Ground": {"Normal": C,
                         "Fire": D,
                         "Water": C,
                         "Electric": D,
                         "Grass": B,
                         "Ice": C,
                         "Fighting": C,
                         "Poison": D,
                         "Ground": C,
                         "Flying": A,
                         "Psychic": C,
                         "Bug": B,
                         "Rock": D,
                         "Ghost": C,
                         "Dragon": C,
                         "Dark": C,
                         "Steel": D,
                         "Fairy": C,
                         "Typeless": C,
                         },
              "Flying": {"Normal": C,
                         "Fire": C,
                         "Water": C,
                         "Electric": B,
                         "Grass": D,
                         "Ice": C,
                         "Fighting": D,
                         "Poison": C,
                         "Ground": C,
                         "Flying": C,
                         "Psychic": C,
                         "Bug": D,
                         "Rock": B,
                         "Ghost": C,
                         "Dragon": C,
                         "Dark": C,
                         "Steel": B,
                         "Fairy": C,
                         "Typeless": C,
                         },
              "Psychic": {"Normal": C,
                          "Fire": C,
                          "Water": C,
                          "Electric": C,
                          "Grass": C,
                          "Ice": C,
                          "Fighting": D,
                          "Poison": D,
                          "Ground": C,
                          "Flying": C,
                          "Psychic": B,
                          "Bug": C,
                          "Rock": C,
                          "Ghost": C,
                          "Dragon": C,
                          "Dark": A,
                          "Steel": B,
                          "Fairy": C,
                          "Typeless": C,
                          },
              "Bug": {"Normal": C,
                      "Fire": B,
                      "Water": C,
                      "Electric": C,
                      "Grass": D,
                      "Ice": C,
                      "Fighting": B,
                      "Poison": B,
                      "Ground": C,
                      "Flying": B,
                      "Psychic": D,
                      "Bug": C,
                      "Rock": C,
                      "Ghost": B,
                      "Dragon": C,
                      "Dark": D,
                      "Steel": B,
                      "Fairy": B,
                      "Typeless": C,
                      },
              "Rock": {"Normal": C,
                       "Fire": D,
                       "Water": C,
                       "Electric": C,
                       "Grass": C,
                       "Ice": D,
                       "Fighting": B,
                       "Poison": C,
                       "Ground": B,
                       "Flying": D,
                       "Psychic": C,
                       "Bug": D,
                       "Rock": C,
                       "Ghost": C,
                       "Dragon": C,
                       "Dark": C,
                       "Steel": B,
                       "Fairy": C,
                       "Typeless": C,
                       },
              "Ghost": {"Normal": A,
                        "Fire": C,
                        "Water": C,
                        "Electric": C,
                        "Grass": C,
                        "Ice": C,
                        "Fighting": C,
                        "Poison": C,
                        "Ground": C,
                        "Flying": C,
                        "Psychic": D,
                        "Bug": C,
                        "Rock": C,
                        "Ghost": D,
                        "Dragon": C,
                        "Dark": B,
                        "Steel": C,
                        "Fairy": C,
                        "Typeless": C,
                        },
              "Dragon": {"Normal": C,
                         "Fire": C,
                         "Water": C,
                         "Electric": C,
                         "Grass": C,
                         "Ice": C,
                         "Fighting": C,
                         "Poison": C,
                         "Ground": C,
                         "Flying": C,
                         "Psychic": C,
                         "Bug": C,
                         "Rock": C,
                         "Ghost": C,
                         "Dragon": D,
                         "Dark": C,
                         "Steel": B,
                         "Fairy": A,
                         "Typeless": C,
                         },
              "Dark": {"Normal": C,
                       "Fire": C,
                       "Water": C,
                       "Electric": C,
                       "Grass": C,
                       "Ice": C,
                       "Fighting": B,
                       "Poison": C,
                       "Ground": C,
                       "Flying": C,
                       "Psychic": D,
                       "Bug": C,
                       "Rock": C,
                       "Ghost": D,
                       "Dragon": C,
                       "Dark": B,
                       "Steel": C,
                       "Fairy": B,
                       "Typeless": C,
                       },
              "Steel": {"Normal": C,
                        "Fire": B,
                        "Water": B,
                        "Electric": B,
                        "Grass": C,
                        "Ice": D,
                        "Fighting": C,
                        "Poison": C,
                        "Ground": C,
                        "Flying": C,
                        "Psychic": C,
                        "Bug": C,
                        "Rock": D,
                        "Ghost": C,
                        "Dragon": C,
                        "Dark": C,
                        "Steel": B,
                        "Fairy": D,
                        "Typeless": C,
                        },
              "Fairy": {"Normal": C,
                        "Fire": B,
                        "Water": C,
                        "Electric": C,
                        "Grass": C,
                        "Ice": C,
                        "Fighting": D,
                        "Poison": B,
                        "Ground": C,
                        "Flying": C,
                        "Psychic": C,
                        "Bug": C,
                        "Rock": C,
                        "Ghost": C,
                        "Dragon": D,
                        "Dark": D,
                        "Steel": B,
                        "Fairy": C,
                        "Typeless": C,
                        },
              "Typeless": {"Normal": C,
                           "Fire": C,
                           "Water": C,
                           "Electric": C,
                           "Grass": C,
                           "Ice": C,
                           "Fighting": C,
                           "Poison": C,
                           "Ground": C,
                           "Flying": C,
                           "Psychic": C,
                           "Bug": C,
                           "Rock": C,
                           "Ghost": C,
                           "Dragon": C,
                           "Dark": C,
                           "Steel": C,
                           "Fairy": C,
                           "Typeless": C,
                           },
              }
