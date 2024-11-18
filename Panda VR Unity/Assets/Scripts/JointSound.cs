using System.Linq;
using RosMessageTypes.Geometry;
using RosMessageTypes.PandaMoveit;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;
using UnityEngine;

public class JointSound : MonoBehaviour
{
    const int k_NumRobotJoints = 7;

    [SerializeField]
    GameObject m_Panda;
    public GameObject Panda { get => m_Panda; set => m_Panda = value; }

    ArticulationBody[] m_JointArticulationBodies;

    public AudioClip jointSound;
    AudioSource[] m_AudioSources;

    float[] m_PreviousVelocities;
    int[] m_StabilityCounters;
    const int stabilityThreshold = 10; 

    void Start()
    {
        m_AudioSources = new AudioSource[k_NumRobotJoints];
        m_JointArticulationBodies = new ArticulationBody[k_NumRobotJoints];
        m_PreviousVelocities = new float[k_NumRobotJoints];
        m_StabilityCounters = new int[k_NumRobotJoints];

        var linkName = string.Empty;
        for (var i = 0; i < k_NumRobotJoints; i++)
        {
            linkName += SourceDestinationPublisher.LinkNames[i];
            m_JointArticulationBodies[i] = m_Panda.transform.Find(linkName).GetComponent<ArticulationBody>();

            m_AudioSources[i] = m_JointArticulationBodies[i].gameObject.AddComponent<AudioSource>();
            m_AudioSources[i].clip = jointSound;
            m_AudioSources[i].loop = true; 

            m_PreviousVelocities[i] = m_JointArticulationBodies[i].xDrive.target;
            m_StabilityCounters[i] = 0;
        }
    }

    void Update()
    {
        for (int i = 0; i < m_JointArticulationBodies.Length; i++)
        {
            var currentVelocity = m_JointArticulationBodies[i].xDrive.target;

            if (currentVelocity != m_PreviousVelocities[i])
            {
                m_StabilityCounters[i] = 0;

                if (!m_AudioSources[i].isPlaying)
                {
                    m_AudioSources[i].Play();
                }
            }

            else
            {
                m_StabilityCounters[i]++;

                if (m_StabilityCounters[i] >= stabilityThreshold && m_AudioSources[i].isPlaying)
                {
                    m_AudioSources[i].Stop();
                }
            }

            m_PreviousVelocities[i] = currentVelocity;
        }
    }
}
